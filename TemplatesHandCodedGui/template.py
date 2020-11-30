import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        username_input = qtw.QLineEdit()
        password_input = qtw.QLineEdit()
        password_input.setEchoMode(qtw.QLineEdit.Password)

        cancel_button = qtw.QPushButton('Cancel')
        submit_button = qtw.QPushButton('Login')

        layout = qtw.QFormLayout()
        layout.addRow('Username', username_input)
        layout.addRow('Password', password_input)

        button_widget = qtw.QWidget()
        button_widget.setLayout(qtw.QHBoxLayout())
        button_widget.layout().addWidget(cancel_button)
        button_widget.layout().addWidget(submit_button)
        layout.addRow('', button_widget)
        self.setLayout(layout)

        # Your code ends here
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
