from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from instrucciones import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

        # Widgets de la columna izquierda
        self.name_label = QLabel(txt_name_label)
        self.name_input = QLineEdit()
        self.age_label = QLabel(txt_age_label)
        self.age_input = QLineEdit()
        self.first_test_instr = QLabel(txt_first_test_instr)
        self.btn_first_test = QPushButton(txt_first_test_btn)
        self.first_test_result = QLineEdit()
        self.squats_instr = QLabel(txt_squats_instr)
        self.btn_squats = QPushButton(txt_squats_btn)
        self.final_test_instr = QLabel(txt_final_test_instr)
        self.btn_final_test = QPushButton(txt_final_test_btn)
        self.final_test_result_1 = QLineEdit()
        self.final_test_result_2 = QLineEdit()
        self.btn_send = QPushButton(txt_send_btn)

        self.l_line.addWidget(self.name_label)
        self.l_line.addWidget(self.name_input)
        self.l_line.addWidget(self.age_label)
        self.l_line.addWidget(self.age_input)
        self.l_line.addWidget(self.first_test_instr)
        self.l_line.addWidget(self.btn_first_test)
        self.l_line.addWidget(self.first_test_result)
        self.l_line.addWidget(self.squats_instr)
        self.l_line.addWidget(self.btn_squats)
        self.l_line.addWidget(self.final_test_instr)
        self.l_line.addWidget(self.btn_final_test)
        self.l_line.addWidget(self.final_test_result_1)
        self.l_line.addWidget(self.final_test_result_2)
        self.l_line.addWidget(self.btn_send)

        # Widget de la columna derecha
        self.timer_label = QLabel('00:00:00')
        self.r_line.addWidget(self.timer_label)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.btn_send.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = FinalWin()
    
app = QApplication([])
mw = TestWin()
app.exec_()