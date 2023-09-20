import sys

from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QWidget()
    label = QtWidgets.QLabel(win)
    btn = QtWidgets.QPushButton(win)
    edit = QtWidgets.QLineEdit(win)

    win.setWindowTitle("First app")
    win.setGeometry(100, 100, 400, 200)

    label.setText("Hello World")
    btn.setText("Send")

    label.move(150, 50)
    btn.move(160, 120)
    edit.move(110, 80)

    win.show()
    app.exec_()


window()