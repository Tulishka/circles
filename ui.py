from PyQt6.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt6.QtWidgets import QPushButton


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(585, 427)
        self.draw = QPushButton(Form)
        self.draw.setObjectName(u"draw")
        self.draw.setGeometry(QRect(230, 180, 101, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.draw.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0440\u0438\u0441\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi
