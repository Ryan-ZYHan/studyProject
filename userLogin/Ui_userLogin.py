# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userLogin.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_userLoginWindow(object):
    def setupUi(self, userLoginWindow):
        if not userLoginWindow.objectName():
            userLoginWindow.setObjectName(u"userLoginWindow")
        userLoginWindow.resize(402, 194)
        self.centralwidget = QWidget(userLoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(60, 60, 261, 66))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.ledt_userName = QLineEdit(self.formLayoutWidget)
        self.ledt_userName.setObjectName(u"ledt_userName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ledt_userName)

        self.ledt_password = QLineEdit(self.formLayoutWidget)
        self.ledt_password.setObjectName(u"ledt_password")
        self.ledt_password.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ledt_password)

        self.pbtn_login = QPushButton(self.centralwidget)
        self.pbtn_login.setObjectName(u"pbtn_login")
        self.pbtn_login.setGeometry(QRect(70, 140, 75, 24))
        self.pbtn_reset = QPushButton(self.centralwidget)
        self.pbtn_reset.setObjectName(u"pbtn_reset")
        self.pbtn_reset.setGeometry(QRect(250, 140, 75, 24))
        userLoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(userLoginWindow)
        self.statusbar.setObjectName(u"statusbar")
        userLoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(userLoginWindow)

        QMetaObject.connectSlotsByName(userLoginWindow)
    # setupUi

    def retranslateUi(self, userLoginWindow):
        userLoginWindow.setWindowTitle(QCoreApplication.translate("userLoginWindow", u"\u7528\u6237\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("userLoginWindow", u"\u7528\u6237\u540d\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("userLoginWindow", u"\u5bc6   \u7801\uff1a", None))
        self.pbtn_login.setText(QCoreApplication.translate("userLoginWindow", u"\u767b\u5f55", None))
        self.pbtn_reset.setText(QCoreApplication.translate("userLoginWindow", u"\u91cd\u7f6e", None))
    # retranslateUi

