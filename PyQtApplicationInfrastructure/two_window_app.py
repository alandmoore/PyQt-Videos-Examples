"""Simple test application for dealing with multiple windows"""
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

LABEL_TEXT = 'Hi There'

class MainApp(qtw.QApplication):
    """The main application object"""
    def __init__(self, argv):
        super().__init__(argv)

        # create main window
        self.main_window = MainWindow()
        self.main_window.show()

        # create settings dialog
        self.settings_dialog = SettingDialog()
        self.main_window.settings_requested.connect(self.settings_dialog.show)
        self.settings_dialog.text_submitted.connect(self.main_window.change_text)

class SettingDialog(qtw.QWidget):
    """The settings dialog window"""

    text_submitted = qtc.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.input = qtw.QLineEdit()
        self.submit = qtw.QPushButton("Submit", clicked=self._on_submit)

        self.setLayout(qtw.QHBoxLayout())
        self.layout().addWidget(self.input)
        self.layout().addWidget(self.submit)

    def _on_submit(self):
        text = self.input.text()
        self.text_submitted.emit(text)
        self.close()


class MainWindow(qtw.QWidget):
    """The main application window"""

    settings_requested = qtc.pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.label = qtw.QLabel(LABEL_TEXT)
        self.settings_button = qtw.QPushButton(
            'Settings',
            clicked=self.settings_requested
        )

        self.setLayout(qtw.QVBoxLayout())
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.settings_button)

    def change_text(self, text):
        self.label.setText(text)

if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec())
