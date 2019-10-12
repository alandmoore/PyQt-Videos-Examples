import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

import resources

class SearchWidget(qtw.QWidget):

    submitted = qtc.pyqtSignal(str, bool)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLayout(qtw.QFormLayout())
        self.term_input = qtw.QLineEdit()
        self.case_checkbox = qtw.QCheckBox('Match case')
        search_image = qtg.QPixmap(':/images/search.svg')
        gear_image = qtg.QPixmap(':/images/gear.svg')
        search_icon = qtg.QIcon(search_image)
        search_icon.addPixmap(gear_image, qtg.QIcon.Disabled)
        self.submit_button = qtw.QPushButton(
            'Submit',
            icon=search_icon,
            clicked=self.on_submit,
            objectName='submitbutton'
        )
        self.submit_button.setEnabled(False)
        self.layout().addRow(qtw.QLabel(pixmap=search_image))
        self.layout().addRow('Search', self.term_input)
        self.layout().addRow(self.case_checkbox)
        self.layout().addRow('', self.submit_button)

        self.term_input.textChanged.connect(self.check_term)

    def check_term(self, term):

        if term:
            self.submit_button.setEnabled(True)
        else:
            self.submit_button.setEnabled(False)

    def on_submit(self):
        term = self.term_input.text()
        do_case = (
            self.case_checkbox.checkState() == qtc.Qt.Checked
        )
        self.submitted.emit(term, do_case)


class MainWindow(qtw.QMainWindow):

    def __init__(self):
        """MainWindow constructor."""
        super().__init__()

        # Central Widget
        self.textedit = qtw.QTextEdit()
        self.setCentralWidget(self.textedit)
        print(self.textedit.styleSheet())
        # Menu Bar

        menu = self.menuBar() # -> QMenuBar
        file_menu = menu.addMenu('File') # -> QMenu
        save_act = file_menu.addAction('Save', self.save) # -> QAction
        # Add keyboard shortcuts using QKeySequence constants
        file_menu.addAction(
            'Open',
            self.open,
            # This uses a platform-appropriate Open shortcut:
            qtg.QKeySequence.Open
            )

        # Add a shortcut after the fact:
        save_act.setShortcut(qtg.QKeySequence.Save)
        file_menu.addSeparator()
        file_menu.addAction(
            'Quit',
            self.close,
            qtg.QKeySequence.Quit
        )

        # ToolBar
        edit_toolbar = self.addToolBar('Edit')
        # To use an icon, add it in as the first argument

        copy_icon = qtg.QIcon(qtg.QPixmap(':/images/copy-image.svg'))
        cut_pixmap = qtg.QPixmap(':/images/cut.svg')
        undo_icon = qtg.QIcon(qtg.QPixmap(':/images/undo.svg'))

        qtg.QIcon.setThemeName('theme that doesnot exist')
        edit_toolbar.addAction(copy_icon, 'copy', self.textedit.copy)
        edit_toolbar.addAction(qtg.QIcon(cut_pixmap), 'cut', self.textedit.cut)
        edit_toolbar.addAction(
            qtg.QIcon(qtg.QPixmap(':/images/paste.svg')),
            'paste',
            self.textedit.paste
        )
        edit_toolbar.addAction(
            qtg.QIcon.fromTheme('edit-undo', undo_icon),
            'undo',
            self.textedit.undo
        )
        edit_toolbar.addAction(
            qtg.QIcon(qtg.QPixmap(':/images/redo.svg')),
            'redo',
            self.textedit.redo
        )

        # Status bar

        self.statusBar().showMessage('Welcome to my text editor', 5000)

        # Dockable widget
        search_dock = qtw.QDockWidget('Search')
        self.addDockWidget(
            qtc.Qt.RightDockWidgetArea,
            search_dock
        )
        # You can prevent a dock from floating, closing
        # Or moving by leaving out any of these items:
        search_dock.setFeatures(
            qtw.QDockWidget.DockWidgetClosable |
            qtw.QDockWidget.DockWidgetMovable |
            qtw.QDockWidget.DockWidgetFloatable
        )

        search_widget = SearchWidget()
        search_dock.setWidget(search_widget)
        search_widget.submitted.connect(self.search)

        self.show()

    def save(self):
        text = self.textedit.toPlainText()
        filename, _ = qtw.QFileDialog.getSaveFileName()
        if filename:
            with open(filename, 'w') as handle:
                handle.write(text)
                self.statusBar().showMessage(f'Saved to {filename}')

    def open(self):
        filename, _ = qtw.QFileDialog.getOpenFileName()
        if filename:
            with open(filename, 'r') as handle:
                text = handle.read()
            self.textedit.clear()
            self.textedit.insertPlainText(text)
            self.textedit.moveCursor(qtg.QTextCursor.Start)
            self.statusBar().showMessage(f'Editing {filename}')

    def search(self, term, case_sensitive=False):
        if case_sensitive:
            cur = self.textedit.find(
                term,
                qtg.QTextDocument.FindCaseSensitively
            )
        else:
            cur = self.textedit.find(term)
        if not cur:
            self.statusBar().showMessage('No matches Found', 2000)

stylesheet = """
QTextEdit {
   background-image: url('tile.png');
   font-size: 16pt;
}

QWidget {
   background-color: lightblue;
}

#submitbutton {
    border: 2px solid red;
    background-color: darkred;

}

QCheckBox::indicator:checked {
   background-color: green;
}

QCheckBox::indicator:unchecked {
   background-color: red;
}

QPushButton:hover {
   background-color: red;
}

"""

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    mw = MainWindow()
    sys.exit(app.exec())
