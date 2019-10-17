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

class Worker(qtc.QObject):

    hashed = qtc.pyqtSignal(str, str)

    @qtc.pyqtSlot(str)
    def hash_directory(self, root):
        hash_gen = recursive_hashes(Path(root))
        for path, sha1_hash in hash_gen:
            self.hashed.emit(path, sha1_hash)

class MainWindow(qtw.QMainWindow):

    hash_requested = qtc.pyqtSignal(str)

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

        # Create a worker object and a thread
        self.worker = Worker()
        self.worker_thread = qtc.QThread()
        self.worker.hashed.connect(self.add_hash_to_table)
        self.hash_requested.connect(self.worker.hash_directory)

        # Assign the worker to the thread and start the thread
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()

        # Connect signals & slots AFTER moving the object to the thread


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
        """Prepare the GUI and emit the hash_requested signal"""

        # Clear the table
        while self.results.rowCount() > 0:
            self.results.removeRow(0)

        # Get the file root and validate it
        file_root = self.file_root.text()
        if not Path(file_root).exists():
            qtw.QMessageBox.critical(self, 'Invalid Path', 'The specified file root does not exist.')
            return

        # Emit the signal
        self.hash_requested.emit(file_root)
        #self.worker.hash_directory(file_root)




if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())


######################
# Things to Note     #
######################

# 1. Only communicate with the Worker via Signals & Slots
#   - Do not call any of its methods from the main thread
#   - Think about your class design so that you can directly connect things

# 2. Connect signals AFTER you move the object to its own thread
#   - Or, wrap all the Worker's methods in pyqtSlot()
#

# 3. Beware the GIL!
#   - Threading is OK for I/O bound loads
#   - Threading is OK for CPU bound loads implemented outside Python
#   - Threading is not OK for CPU bound loads implemented in Python
