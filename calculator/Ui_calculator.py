# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_calculatorForm(object):
    def setupUi(self, calculatorForm):
        if not calculatorForm.objectName():
            calculatorForm.setObjectName(u"calculatorForm")
        calculatorForm.resize(421, 250)
        self.formLayoutWidget = QWidget(calculatorForm)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 120, 331, 124))
        self.gridLayout = QGridLayout(self.formLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.pbtn_7 = QPushButton(self.formLayoutWidget)
        self.pbtn_7.setObjectName(u"pbtn_7")

        self.gridLayout.addWidget(self.pbtn_7, 2, 0, 1, 1)

        self.pbtn_backspace = QPushButton(self.formLayoutWidget)
        self.pbtn_backspace.setObjectName(u"pbtn_backspace")

        self.gridLayout.addWidget(self.pbtn_backspace, 3, 2, 1, 1)

        self.pbtn_dot = QPushButton(self.formLayoutWidget)
        self.pbtn_dot.setObjectName(u"pbtn_dot")

        self.gridLayout.addWidget(self.pbtn_dot, 3, 1, 1, 1)

        self.pbtn_1 = QPushButton(self.formLayoutWidget)
        self.pbtn_1.setObjectName(u"pbtn_1")

        self.gridLayout.addWidget(self.pbtn_1, 0, 0, 1, 1)

        self.pbtn_4 = QPushButton(self.formLayoutWidget)
        self.pbtn_4.setObjectName(u"pbtn_4")

        self.gridLayout.addWidget(self.pbtn_4, 1, 0, 1, 1)

        self.pbtn_sub = QPushButton(self.formLayoutWidget)
        self.pbtn_sub.setObjectName(u"pbtn_sub")

        self.gridLayout.addWidget(self.pbtn_sub, 1, 3, 1, 1)

        self.pbtn_9 = QPushButton(self.formLayoutWidget)
        self.pbtn_9.setObjectName(u"pbtn_9")

        self.gridLayout.addWidget(self.pbtn_9, 2, 2, 1, 1)

        self.pbtn_6 = QPushButton(self.formLayoutWidget)
        self.pbtn_6.setObjectName(u"pbtn_6")

        self.gridLayout.addWidget(self.pbtn_6, 1, 2, 1, 1)

        self.pbtn_mul = QPushButton(self.formLayoutWidget)
        self.pbtn_mul.setObjectName(u"pbtn_mul")

        self.gridLayout.addWidget(self.pbtn_mul, 2, 3, 1, 1)

        self.pbtn_3 = QPushButton(self.formLayoutWidget)
        self.pbtn_3.setObjectName(u"pbtn_3")

        self.gridLayout.addWidget(self.pbtn_3, 0, 2, 1, 1)

        self.pbtn_8 = QPushButton(self.formLayoutWidget)
        self.pbtn_8.setObjectName(u"pbtn_8")

        self.gridLayout.addWidget(self.pbtn_8, 2, 1, 1, 1)

        self.pbtn_add = QPushButton(self.formLayoutWidget)
        self.pbtn_add.setObjectName(u"pbtn_add")

        self.gridLayout.addWidget(self.pbtn_add, 0, 3, 1, 1)

        self.pbtn_0 = QPushButton(self.formLayoutWidget)
        self.pbtn_0.setObjectName(u"pbtn_0")

        self.gridLayout.addWidget(self.pbtn_0, 3, 0, 1, 1)

        self.pbtn_5 = QPushButton(self.formLayoutWidget)
        self.pbtn_5.setObjectName(u"pbtn_5")

        self.gridLayout.addWidget(self.pbtn_5, 1, 1, 1, 1)

        self.pbtn_2 = QPushButton(self.formLayoutWidget)
        self.pbtn_2.setObjectName(u"pbtn_2")

        self.gridLayout.addWidget(self.pbtn_2, 0, 1, 1, 1)

        self.pbtn_div = QPushButton(self.formLayoutWidget)
        self.pbtn_div.setObjectName(u"pbtn_div")
        self.pbtn_div.setBaseSize(QSize(0, 0))
        self.pbtn_div.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.pbtn_div, 3, 3, 1, 1)

        self.txt_display = QTextEdit(calculatorForm)
        self.txt_display.setObjectName(u"txt_display")
        self.txt_display.setGeometry(QRect(0, 0, 421, 121))
        self.verticalLayoutWidget = QWidget(calculatorForm)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(330, 120, 85, 121))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.pbtn_equal = QPushButton(self.verticalLayoutWidget)
        self.pbtn_equal.setObjectName(u"pbtn_equal")
        self.pbtn_equal.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbtn_equal.sizePolicy().hasHeightForWidth())
        self.pbtn_equal.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pbtn_equal)

        self.pbtn_clear = QPushButton(self.verticalLayoutWidget)
        self.pbtn_clear.setObjectName(u"pbtn_clear")
        sizePolicy.setHeightForWidth(self.pbtn_clear.sizePolicy().hasHeightForWidth())
        self.pbtn_clear.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pbtn_clear)


        self.retranslateUi(calculatorForm)

        QMetaObject.connectSlotsByName(calculatorForm)
    # setupUi

    def retranslateUi(self, calculatorForm):
        calculatorForm.setWindowTitle(QCoreApplication.translate("calculatorForm", u"\u8ba1\u7b97\u5668", None))
        self.pbtn_7.setText(QCoreApplication.translate("calculatorForm", u"7", None))
        self.pbtn_backspace.setText(QCoreApplication.translate("calculatorForm", u"bs", None))
        self.pbtn_dot.setText(QCoreApplication.translate("calculatorForm", u".", None))
        self.pbtn_1.setText(QCoreApplication.translate("calculatorForm", u"1", None))
        self.pbtn_4.setText(QCoreApplication.translate("calculatorForm", u"4", None))
        self.pbtn_sub.setText(QCoreApplication.translate("calculatorForm", u"-", None))
        self.pbtn_9.setText(QCoreApplication.translate("calculatorForm", u"9", None))
        self.pbtn_6.setText(QCoreApplication.translate("calculatorForm", u"6", None))
        self.pbtn_mul.setText(QCoreApplication.translate("calculatorForm", u"*", None))
        self.pbtn_3.setText(QCoreApplication.translate("calculatorForm", u"3", None))
        self.pbtn_8.setText(QCoreApplication.translate("calculatorForm", u"8", None))
        self.pbtn_add.setText(QCoreApplication.translate("calculatorForm", u"+", None))
        self.pbtn_0.setText(QCoreApplication.translate("calculatorForm", u"0", None))
        self.pbtn_5.setText(QCoreApplication.translate("calculatorForm", u"5", None))
        self.pbtn_2.setText(QCoreApplication.translate("calculatorForm", u"2", None))
        self.pbtn_div.setText(QCoreApplication.translate("calculatorForm", u"/", None))
        self.pbtn_equal.setText(QCoreApplication.translate("calculatorForm", u"\u8ba1\u7b97", None))
        self.pbtn_clear.setText(QCoreApplication.translate("calculatorForm", u"\u6e05\u7a7a", None))
    # retranslateUi

