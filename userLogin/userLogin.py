"""
登录界面
"""
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from Ui_userLogin import Ui_userLoginWindow
from Func_userLoginMethod import Func_userLoginMethod


class UserLoginWindow(QMainWindow,Ui_userLoginWindow,Func_userLoginMethod):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupFunc()
        

if __name__ == "__main__":
    app = QApplication([])
    window = UserLoginWindow()
    window.show()
    app.exec()