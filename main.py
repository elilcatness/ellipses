import sys
from random import randint

from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor, QFont


class Ui_Form:
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 573)
        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(QRect(240, 520, 111, 41))
        font = QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Жёлтые окружности"))
        self.pushButton.setText(_translate("Form", "Нарисовать"))


class Window(QWidget, Ui_Form):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        self.paint = False
        self.ellipses = []

        self.pushButton.clicked.connect(self.draw_ellipse)

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(241, 237, 65))
            for el in self.ellipses:
                qp.drawEllipse(*el)
            side = randint(30, 250)
            window_size = self.size()
            window_height, window_width = window_size.height(), window_size.width()
            x, y = [randint(0, 600) for _ in range(2)]
            if x + side > window_width:
                x = (x + side) % window_width
            elif x - side < 0:
                x = window_width - side
            if y + side > window_height:
                y = (y + side) % window_height
            elif y - side < 0:
                y = window_height - side
            qp.drawEllipse(x, y, side, side)
            self.ellipses.append((x, y, side, side))

    def draw_ellipse(self):
        self.paint = True
        self.repaint()
        self.paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())