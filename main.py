import random
import sys

from PyQt6.QtGui import QPainter, QColor
from UI import UI
from PyQt6.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow, UI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setBrush(QColor(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        a = random.randint(10, 300)
        qp.drawEllipse(125, 100, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())