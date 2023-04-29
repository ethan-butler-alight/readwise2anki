from aqt.qt import *

app = QApplication([])
label = QLabel("Hello world!")
label.show()

button = QPushButton("Say hello")


def say_hello(event):
    print("Hello, world")


button.clicked.connect(say_hello)
button.show()
app.exec_()
