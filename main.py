import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('Ui.ui', self)

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