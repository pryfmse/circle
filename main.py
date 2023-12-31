from PyQt5 import QtWidgets

from sys import argv, exit
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from ui import Ui_MainWindow


class Suprematism(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setupUi(self)
        self.w = QtWidgets.QWidget(self)
        self.setCentralWidget(self.w)
        self.button = QPushButton(self)
        self.button.move(300, 400)
        self.qp = QPainter()

        self.k = 0
        self.button.clicked.connect(self.do)

    def do(self):
        self.k = 1
        self.update()

    def paintEvent(self, event):
        self.qp.begin(self)
        self.drawing(self.qp)
        self.qp.end()

    def drawing(self, qp):
        if self.k == 1:
            a = float(randint(20, 100))
            x = randint(20, 400)
            y = randint(20, 400)

            qp.setBrush(QColor(randint(1, 255), randint(1, 255), randint(1, 255)))
            qp.drawEllipse(QPoint(x, y), a, a)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Suprematism()
    ex.show()
    exit(app.exec())
