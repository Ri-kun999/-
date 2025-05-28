from PyQt5.Qtcore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout. QGroupbox, QradioButton, QPushButton, QLabel, QlistWidget, QLineEdit)

from instr import *

class FinalWin(QWidget):
    def __init_(self):
        super().__init_()
        self.initUI()
        self.set_appear()
        self.show()

    def initUI(self):
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)
        
        self.Layout_Time = QVBoxLayout()
        self.Layout_Time.addWidget(self.index_text, alignment = QL. AlignCenter)
        self.Layout_Time.addWidget(self.work_text, alignment = Qt. AlignCenter)
        self.setLayout(self.Layout_line)

    def set_appear(self):
        self.setWindowtitle(txt_finalWin)
        self.resize(win_widtn, win_height)
        self.move(win_x, win_y)