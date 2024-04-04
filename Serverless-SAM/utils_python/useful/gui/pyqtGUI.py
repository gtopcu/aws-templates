
# https://pypi.org/project/PyQt5/
# pip install PyQt5

# mandelbrot

"""
This code creates a simple GUI using PyQt5 and displays a fixed-size Mandelbrot set. You can zoom in by modifying the 
xmin, xmax, ymin, and ymax values and then updating the Mandelbrot set accordingly. Additionally, you might want to 
implement zooming functionality through mouse events or buttons to make the GUI infinitely zoomable.

"""

import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QColor
# from PyQt5.QtGui import QImage, QPixmap, QPainter, QColor, QPen, QBrush
# from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QRectF, QPointF, QLineF, QObject, pyqtSignal, pyqtSlot, QThread
# from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot, QRunnable, QThreadPool, QTimer, QCoreApplication



def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            img[i, j] = mandelbrot(complex(x[i], y[j]), max_iter)
    return img

class MandelbrotWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.xmin, self.xmax = -2.0, 2.0
        self.ymin, self.ymax = -2.0, 2.0
        self.width, self.height = 400, 400
        self.max_iter = 1000
        self.image = mandelbrot_set(self.xmin, self.xmax, self.ymin, self.ymax, self.width, self.height, self.max_iter)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.create_image()))

    def create_image(self):
        qimg = QPixmap(self.width, self.height)
        painter = QPainter(qimg)
        for i in range(self.width):
            for j in range(self.height):
                color = QColor(self.image[i, j] % 256, 0, 0)
                painter.setPen(color)
                painter.drawPoint(i, j)
        painter.end()
        return qimg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mandelbrot Viewer")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.mandelbrot_widget = MandelbrotWidget()
        self.layout.addWidget(self.mandelbrot_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 400, 400)
    window.show()
    sys.exit(app.exec_())
