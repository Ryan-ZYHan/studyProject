"""
界面登录的所有方法
"""
from PySide6.QtWidgets import QMessageBox

from entity.userEntity import User
from dao import userDao
from bookManagement.bookManagement import BookManagerWindow

class Func_userLoginMethod(object):
    def setupFunc(self):
        self.bind()

    def bind(self):
        self.pbtn_reset.clicked.connect(self.reset)
        self.pbtn_login.clicked.connect(self.login)

    def reset(self):
        self.ledt_userName.clear()
        self.ledt_password.clear()

    def login(self):
        """
        用户登录判断 数据库判断成功，则打开主窗体，否则提示报错信息
        """
        userName = self.ledt_userName.text()
        password = self.ledt_password.text()

        if userName == "" or password == "":
            QMessageBox.warning(self, "提示", "用户名或密码不能为空")
        else:
            user = User(userName, password)
            resultUser = userDao.login(user)
            if resultUser != None:
                # QMessageBox.information(self, "提示", "用户登录成功")
                self.bookManagerWindow =  BookManagerWindow()
                self.bookManagerWindow.show()
                self.hide()
            else:
                QMessageBox.warning(self, "提示", "用户名或密码错误")
