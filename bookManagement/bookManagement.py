"""
图书管理界面
"""
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from bookManagement.Ui_bookManagement import Ui_bookManagementWindow
from bookManagement.Func_bookManagement import Func_bookManagementMethod


class BookManagerWindow(QMainWindow, Ui_bookManagementWindow, Func_bookManagementMethod):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupFunc()


if __name__ == "__main__":
    app = QApplication([])
    window = BookManagerWindow()
    window.show()
    app.exec()
