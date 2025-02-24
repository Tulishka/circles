import sys
from random import randint

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import (
    QApplication, QWidget
)


class Circles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.setWindowTitle('Git и желтые окружности')
        self.circles = []
        self.draw.clicked.connect(self.click_btn)

    def click_btn(self):
        d = randint(0, 100)
        self.circles.append((randint(0, self.width() - d), randint(0, self.height() - d), d))
        self.update()

    def update_drawing(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(255, 255, 0))
        for x, y, d in self.circles:
            qp.drawEllipse(x, y, d, d)
        qp.end()
        super().paintEvent(event)


def func(*args):
    print(*args)
    sys.__excepthook__(*args)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = func
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
