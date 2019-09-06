import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):

    authenticated = qtc.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        self.username_input = qtw.QLineEdit()
        self.password_input = qtw.QLineEdit()
        self.password_input.setEchoMode(
            qtw.QLineEdit.Password)

        self.cancel_button = qtw.QPushButton('Cancel')
        self.submit_button = qtw.QPushButton('Login')

        layout = qtw.QFormLayout()
        layout.addRow('Username', self.username_input)
        layout.addRow('Password', self.password_input)

        button_widget = qtw.QWidget()
        button_widget.setLayout(qtw.QHBoxLayout())
        button_widget.layout().addWidget(self.cancel_button)
        button_widget.layout().addWidget(self.submit_button)
        layout.addRow('', button_widget)
        self.setLayout(layout)

        self.cancel_button.clicked.connect(self.close)
        self.submit_button.clicked.connect(self.authenticate)

        self.username_input.textChanged.connect(self.set_button_text)
        self.authenticated.connect(self.user_logged_in)

        # Your code ends here
        self.show()

    def set_button_text(self, text):
        if text:
            self.submit_button.setText(f'Log In {text}')
        else:
            self.submit_button.setText('Log In')

    def authenticate(self):

        username = self.username_input.text()
        password = self.password_input.text()

        if username == 'user' and password == 'pass':
            qtw.QMessageBox.information(self, 'Success', 'You are logged in.')
            self.authenticated.emit(username)
        else:
            qtw.QMessageBox.critical(self, 'Failed', 'You are not logged in.')

    def user_logged_in(self, username):

        qtw.QMessageBox.information(self, 'Logged in', f'{username} is logged in.')

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
