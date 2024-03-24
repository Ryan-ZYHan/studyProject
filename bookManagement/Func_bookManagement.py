"""
图书管理系统方法
"""
from PySide6.QtWidgets import QLabel

from entity.userEntity import User
from dao import userDao


class Func_bookManagementMethod(object):
    def setupFunc(self):
        self.bind()
        self.setui()

    def bind(self):
        pass

    def setui(self):
        myLabel = QLabel()
        myLabel.setText("当前登录用户为："+userDao.currentUser.userName)
        self.statusbar.addWidget(myLabel)
