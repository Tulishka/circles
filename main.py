import sys
from random import randint

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import (
    QApplication, QWidget
)

from ui import Ui_Form


class Circles(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Git и случайные окружности')

        self.circles = []

        super().setupUi(self)
        self.draw.clicked.connect(self.click_btn)

    def click_btn(self):
        d = randint(0, 100)
        self.circles.append((randint(0, self.width() - d),
                             randint(0, self.height() - d),
                             d,
                             QColor(randint(0, 255), randint(0, 255), randint(0, 255))))
        self.update()

    def update_drawing(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for x, y, d, color in self.circles:
            qp.setPen(color)
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
