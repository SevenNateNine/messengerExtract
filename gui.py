# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QGridLayout, QVBoxLayout, QLabel, QGroupBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import messengerReader

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Message Extract'
        self.left = 300
        self.top = 300
        self.width = 320
        self.height = 100
        self.initUI()
    
    @pyqtSlot()
    def on_click(self):
        email = self.emailText.text()
        password = self.passwordText.text()
        conversation = self.conversationText.text()
        message = self.messageText.text()
        messengerReader.messengerStart(email, password, conversation, message)


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.createGridLayout()

        start_button = QPushButton('Start')
        start_button.clicked.connect(self.on_click)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        windowLayout.addWidget(start_button)
        self.setLayout(windowLayout)
        
        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Credentials")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

        emailLabel = QLabel('Email')
        self.emailText = QLineEdit()
        passwordLabel = QLabel('Password')
        self.passwordText = QLineEdit()
        conversationLabel = QLabel('Conversation Name')
        self.conversationText = QLineEdit()
        messageLabel = QLabel('Search Message')
        self.messageText = QLineEdit()

        layout.addWidget(emailLabel,0,0)
        layout.addWidget(self.emailText,0,1)
        layout.addWidget(passwordLabel,1,0)
        layout.addWidget(self.passwordText,1,1)
        layout.addWidget(conversationLabel,2,0)
        layout.addWidget(self.conversationText,2,1)
        layout.addWidget(messageLabel,3,0)
        layout.addWidget(self.messageText,3,1)

        self.horizontalGroupBox.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())