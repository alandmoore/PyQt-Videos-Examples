import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from pathlib import Path
from hashlib import sha1


def recursive_hashes(path):
    """Generate name and SHA1 hash of all files under the given path"""
    if path.is_file():
        sha1_obj = sha1()
        try:
            with open(path, 'rb') as handle:
                while True:
                    data = handle.read(8192)
                    if not data:
                        break
                    sha1_obj.update(data)
            sha1_hash = sha1_obj.hexdigest()
        except PermissionError:
            sha1_hash = 'Permission Denied'
        yield (str(path), sha1_hash)
    elif path.is_dir():
        try:
            for child in path.iterdir():
                yield from recursive_hashes(child)
        except PermissionError:
            yield(str(path), 'Permission Denied')
    else:
        yield (str(path), 'Not a file or dir')


class MainWindow(qtw.QMainWindow):

    def __init__(self):
        """MainWindow constructor."""
        super().__init__()
        # Main UI code goes here
        form = qtw.QWidget()
        self.setCentralWidget(form)
        layout = qtw.QFormLayout()
        form.setLayout(layout)

        self.file_root = qtw.QLineEdit(returnPressed=self.start_hashing)
        self.go_button = qtw.QPushButton('Start Hashing', clicked=self.start_hashing)
        self.results = qtw.QTableWidget(0, 2)
        self.results.setHorizontalHeaderLabels(['Name', 'SHA1-sum'])
        self.results.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        self.results.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)

        layout.addRow(qtw.QLabel('SHA1 Recursive Hasher'))
        layout.addRow('File Root', self.file_root)
        layout.addRow('', self.go_button)
        layout.addRow(self.results)

        # End main UI code
        self.show()

    def add_hash_to_table(self, name, sha1_sum):
        """Add the given name and sha1 sum to the table"""

        row = self.results.rowCount()
        self.results.insertRow(row)
        self.results.setItem(row, 0, qtw.QTableWidgetItem(name))
        self.results.setItem(row, 1, qtw.QTableWidgetItem(sha1_sum))
        print(name, sha1_sum)

    def start_hashing(self):
        """Start hashing files under the entered directory"""

        # clear the table
        while self.results.rowCount() > 0:
            self.results.removeRow(0)

        # Get the file root and validate it
        file_root = self.file_root.text()
        if not Path(file_root).exists():
            qtw.QMessageBox.critical(self, 'Invalid Path', 'The specified file root does not exist.')
            return

        # Get the generator
        self.hash_gen = recursive_hashes(Path(file_root))

        # Kick off the first hash
        qtc.QTimer.singleShot(0, self.next_hash)


    def next_hash(self):
        """Get the next hash and add it to the table"""

        # Get the next hash
        try:
            name, sha1_sum = next(self.hash_gen)
        except StopIteration:
            return

        # Add it to the table
        self.add_hash_to_table(name, sha1_sum)

        # Put another call to next_hash in the event Queue
        qtc.QTimer.singleShot(0, self.next_hash)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
