import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
class MyWindow(QMainWindow):
def __init__(self):
super(MyWindow, self).__init__()
loadUi("hello_message.ui", self)
self.pushButton.clicked.connect(self.hello)
def hello(self):
name = self.lineEdit.text()
if name:
greeting = f'Hello, {name}!'
else:
greeting = 'Hello, stranger!'
self.label.setText(greeting)
def main():
app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
if __name__ == '__main__':
main()
