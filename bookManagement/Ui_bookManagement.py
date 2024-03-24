# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bookManagement.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_bookManagementWindow(object):
    def setupUi(self, bookManagementWindow):
        if not bookManagementWindow.objectName():
            bookManagementWindow.setObjectName(u"bookManagementWindow")
        bookManagementWindow.resize(800, 600)
        self.act_addBook = QAction(bookManagementWindow)
        self.act_addBook.setObjectName(u"act_addBook")
        self.act_manageBookInfos = QAction(bookManagementWindow)
        self.act_manageBookInfos.setObjectName(u"act_manageBookInfos")
        self.act_addBookType = QAction(bookManagementWindow)
        self.act_addBookType.setObjectName(u"act_addBookType")
        self.act_manageBookTypeInfos = QAction(bookManagementWindow)
        self.act_manageBookTypeInfos.setObjectName(u"act_manageBookTypeInfos")
        self.act_changePassword = QAction(bookManagementWindow)
        self.act_changePassword.setObjectName(u"act_changePassword")
        self.act_exitSafely = QAction(bookManagementWindow)
        self.act_exitSafely.setObjectName(u"act_exitSafely")
        self.act_aboutAuthor = QAction(bookManagementWindow)
        self.act_aboutAuthor.setObjectName(u"act_aboutAuthor")
        self.centralwidget = QWidget(bookManagementWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        bookManagementWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(bookManagementWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menubar.setNativeMenuBar(True)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        bookManagementWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(bookManagementWindow)
        self.statusbar.setObjectName(u"statusbar")
        bookManagementWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.act_addBook)
        self.menu.addAction(self.act_manageBookInfos)
        self.menu_2.addAction(self.act_addBookType)
        self.menu_2.addAction(self.act_manageBookTypeInfos)
        self.menu_3.addAction(self.act_changePassword)
        self.menu_3.addAction(self.act_exitSafely)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.act_aboutAuthor)

        self.retranslateUi(bookManagementWindow)

        QMetaObject.connectSlotsByName(bookManagementWindow)
    # setupUi

    def retranslateUi(self, bookManagementWindow):
        bookManagementWindow.setWindowTitle(QCoreApplication.translate("bookManagementWindow", u"\u56fe\u4e66\u7ba1\u7406\u7cfb\u7edf", None))
        self.act_addBook.setText(QCoreApplication.translate("bookManagementWindow", u"\u56fe\u4e66\u6dfb\u52a0", None))
        self.act_manageBookInfos.setText(QCoreApplication.translate("bookManagementWindow", u"\u56fe\u4e66\u4fe1\u606f\u7ba1\u7406", None))
        self.act_addBookType.setText(QCoreApplication.translate("bookManagementWindow", u"\u56fe\u4e66\u7c7b\u522b\u6dfb\u52a0", None))
        self.act_manageBookTypeInfos.setText(QCoreApplication.translate("bookManagementWindow", u"\u56fe\u4e66\u7c7b\u522b\u4fe1\u606f\u7ba1\u7406", None))
        self.act_changePassword.setText(QCoreApplication.translate("bookManagementWindow", u"\u4fee\u6539\u5bc6\u7801", None))
        self.act_exitSafely.setText(QCoreApplication.translate("bookManagementWindow", u"\u5b89\u5168\u9000\u51fa", None))
        self.act_aboutAuthor.setText(QCoreApplication.translate("bookManagementWindow", u"\u5173\u4e8e\u4f5c\u8005", None))
        self.menu.setTitle(QCoreApplication.translate("bookManagementWindow", u"\u56fe\u4e66\u7ba1\u7406", None))
        self.menu_2.setTitle(QCoreApplication.translate("bookManagementWindow", u"\u56fe\u4e66\u7c7b\u522b\u7ba1\u7406", None))
        self.menu_3.setTitle(QCoreApplication.translate("bookManagementWindow", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
    # retranslateUi

