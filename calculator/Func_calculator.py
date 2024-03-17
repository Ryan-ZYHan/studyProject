# Func_calculator.py
# 计算器功能的所有方法

from PySide6.QtWidgets import QLineEdit,QTextEdit

class Func_calculatorMethod(object):
    def setupFunc(self):
        self.result = ""
        self.bind()

    def append_number(self,number:str):
        self.txt_display.clear()
        self.result += number
        self.txt_display.setText(self.result)
        # print(self.result)
    def equal(self):
        self.txt_display.clear()
        self.txt_display.setText(str(eval(self.result)))
        self.result = ""
    
    def backspace(self):
        self.result = self.result[:-1]
        self.txt_display.clear()
        self.txt_display.setText(self.result)

    def clear(self):
        self.result = ""
        self.txt_display.clear()
        self.txt_display.setText(self.result)

    def bind(self):
        self.pbtn_0.clicked.connect(lambda:self.append_number('0'))
        self.pbtn_1.clicked.connect(lambda:self.append_number('1'))
        self.pbtn_2.clicked.connect(lambda:self.append_number('2'))
        self.pbtn_3.clicked.connect(lambda:self.append_number('3'))
        self.pbtn_4.clicked.connect(lambda:self.append_number('4'))
        self.pbtn_5.clicked.connect(lambda:self.append_number('5'))
        self.pbtn_6.clicked.connect(lambda:self.append_number('6'))
        self.pbtn_7.clicked.connect(lambda:self.append_number('7'))
        self.pbtn_8.clicked.connect(lambda:self.append_number('8'))
        self.pbtn_9.clicked.connect(lambda:self.append_number('9')) 
        self.pbtn_add.clicked.connect(lambda:self.append_number('+'))
        self.pbtn_sub.clicked.connect(lambda:self.append_number('-'))
        self.pbtn_mul.clicked.connect(lambda:self.append_number('*'))
        self.pbtn_div.clicked.connect(lambda:self.append_number('/'))
        self.pbtn_dot.clicked.connect(lambda:self.append_number('.'))
        self.pbtn_equal.clicked.connect(self.equal)
        self.pbtn_backspace.clicked.connect(self.backspace)
        
    