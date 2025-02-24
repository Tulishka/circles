import io
import sys
from random import randint

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import (
    QApplication, QWidget
)

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>585</width>
    <height>427</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="draw">
   <property name="geometry">
    <rect>
     <x>230</x>
     <y>180</y>
     <width>101</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>Нарисовать</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Circles(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
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
