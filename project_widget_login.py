# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_widget_login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(611, 735)
        font = QFont()
        font.setPointSize(9)
        Login.setFont(font)
        self.horizontalLayout = QHBoxLayout(Login)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.loginFrame = QFrame(Login)
        self.loginFrame.setObjectName(u"loginFrame")
        self.loginFrame.setStyleSheet(u"background-color: rgb(28, 26, 63);")
        self.loginFrame.setFrameShape(QFrame.StyledPanel)
        self.loginFrame.setFrameShadow(QFrame.Raised)
        self.input_user = QLineEdit(self.loginFrame)
        self.input_user.setObjectName(u"input_user")
        self.input_user.setGeometry(QRect(70, 340, 411, 31))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.input_user.setFont(font1)
        self.input_user.setStyleSheet(u"background-color: rgb(35, 173, 237);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px")
        self.input_user.setEchoMode(QLineEdit.Normal)
        self.input_user.setAlignment(Qt.AlignCenter)
        self.input_password = QLineEdit(self.loginFrame)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setGeometry(QRect(70, 430, 411, 31))
        self.input_password.setFont(font1)
        self.input_password.setStyleSheet(u"background-color: rgb(35, 173, 237);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px")
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setAlignment(Qt.AlignCenter)
        self.button_login = QPushButton(self.loginFrame)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setGeometry(QRect(80, 590, 411, 51))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setBold(True)
        font2.setItalic(False)
        self.button_login.setFont(font2)
        self.button_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_login.setStyleSheet(u"QPushButton {\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"	color: rgb(0, 255, 255);\n"
"	background-color: rgb(1, 3, 38);\n"
"	border-radius: 10px;\n"
"	font-size: 20px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(23, 32, 38);\n"
"	background-color: rgb(35, 173, 237);\n"
"}\n"
"")
        self.label = QLabel(self.loginFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 100, 171, 161))
        self.label.setPixmap(QPixmap(u"../files/login-user.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.loginFrame)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.input_user.setText("")
        self.input_user.setPlaceholderText(QCoreApplication.translate("Login", u"User", None))
        self.input_password.setText("")
        self.input_password.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
        self.button_login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.label.setText("")
    # retranslateUi

