import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush

import random


class Example(QWidget):

    def __init__(self):
        self.start = False
        super().__init__()
        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Оккультные кружки')
        self.show()
        self.btn = QPushButton('Не жми - опасно', self)
        self.btn.resize(100, 25)
        self.btn.show()
        self.btn.clicked.connect(self.run)
        
    def run(self):
        self.start = not(self.start)
        self.update()

    def paintEvent(self, e):
        if self.start:
            qp = QPainter()
            qp.begin(self)
            col = QColor(0, 0, 0)
            col.setNamedColor('#ffff00')
            qp.setPen(col)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            rx, ry = random.randint(30, 270), random.randint(30, 270)
            rw = random.randint(10, 60)
            
            qp.drawEllipse(rx, ry, rw, rw)
            qp.end()
            self.update()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
