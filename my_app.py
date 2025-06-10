# напиши здесь код основного приложения и первого экрана
from PQt5.QtCore import Qt, QTimer, QTime, Qlocale
from PyQt5.QtGui import QDoubleValidator, QintValidator, QFont)
from PyQt5.QtWidgets import(QApplication, Qwidget, QHBoxLayout, QVBoxLayout.QGridLayout, QGroupbox, QRadioButton, QPushButton, QLabel, QlistWidget, QLineEdit)
from instr import *
from second_win import *

class MaiWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initui()
        self.connects()
        self.show()
    def initui(self):
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        self.layout = QVBoxLayout()
        self.layout.addwidget(self.hello_text, aligment = Qt.AlignLeft)
        self.layout.addwidget(self.instruction, aligment = Qt.AlignLeft)
        self.layout.addwidget(self.btn_next, aligment = Qt.AlignCenter)
        self.setLayout(self.layout)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
def main():
    app = QApplication([])
    mw = MaiWin()
    app.exec_()

main()
