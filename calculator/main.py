"""
计算器
"""
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from Ui_calculator import Ui_calculatorForm
from Func_calculator import Func_calculatorMethod

class MyWindow(QMainWindow,Ui_calculatorForm,Func_calculatorMethod):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # 加载计算器窗体
        self.setupFunc()

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()