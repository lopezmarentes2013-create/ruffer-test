from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from instrucciones import *
from second_win import *
class Mainwin (QWidget):
    def __init__(self):
        super().__init__()
        self.set_Appear()
        self.initUI()
        self.connects()
        self.show()
        
    def set_Appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    
    def initUI(self):
        self.hello_text = QLabel("txt_hello")
        self.instruction = QLabel("txt_instruction")
        self.btn_next = QLabel("txt_next")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.btn_next)
        self.setLayout(self.layout)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    
    def next_click(self):
        self.hide()
        self.tw = TestWin()


app = QApplication([])
mw = Mainwin()
app.exec_()