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

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 140, 75, 24))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(250, 140, 75, 24))
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
        self.pushButton.setText(QCoreApplication.translate("userLoginWindow", u"\u767b\u5f55", None))
        self.pushButton_2.setText(QCoreApplication.translate("userLoginWindow", u"\u91cd\u7f6e", None))
    # retranslateUi

