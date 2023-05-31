import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 250, 250)
        self.layout = QGridLayout()
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.display, 0, 0, 1, 4)
        self.add_button("7", 1, 0)
        self.add_button("8", 1, 1)
        self.add_button("9", 1, 2)
        self.add_button("/", 1, 3)
        self.add_button("4", 2, 0)
        self.add_button("5", 2, 1)
        self.add_button("6", 2, 2)
        self.add_button("*", 2, 3)
        self.add_button("1", 3, 0)
        self.add_button("2", 3, 1)
        self.add_button("3", 3, 2)
        self.add_button("-", 3, 3)
        self.add_button("0", 4, 0)
        self.add_button(".", 4,1)
        self.add_button("=", 4, 2)
        self.add_button("+", 4, 3)
        self.add_button("C", 5, 0, 1, 4)
        self.setLayout(self.layout)

    def add_button(self, label, row, col, rowspan=1, colspan=1):
        button = QPushButton(label)
        button.clicked.connect(lambda: self.handle_click(label))
        self.layout.addWidget(button, row, col, rowspan, colspan)

    def handle_click(self, label):
        if label == "C":
            self.display.setText("")
        elif label == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())