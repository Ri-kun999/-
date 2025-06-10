from PyQt5.Qtcore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout. QGroupbox, QradioButton, QPushButton, QLabel, QlistWidget, QLineEdit)

from instr import *
from final_win import *

class testWin(Qwidget):
    def __init_(self)
    self.initUI()
    self.connercts()
    self,set_appear()
    self.show()

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWinTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_text1 = QPushButton(txt_sendresults1 self)
        self.btn_text2 = QPushButton(txt_sendresult2, self)
        self.btn_text1 = QPushButton(txt_sendresult3, self)

        self.text_name = QLavel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)

        self.text_timer = QlineEdit(txt_timer)
        
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QlineEdit(txt_hintage)
        self.line_test1 = QlineEdit(txt_hinttest1)
        self.line_test2 = QlineEdit(txt_hinttest2)
        self.line_test3 = QlineEdit(txt_hinttest3)
        
        self.h_line = QHBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()

        self.r_line.addWidget(self.text_timer, alignment - QL.AlignCenter)
        self.l_line.addWidget(self.text_timer, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self,l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next, alingment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def next_click(self):
        self.hide()
        self.fw = FinalWin()
        
    def connect(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowtitle(txt_title)
        self.resize(win_wight, win_height)
        self.move(win_x, win_y)
        
