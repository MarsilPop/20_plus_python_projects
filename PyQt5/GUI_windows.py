import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Window")
        self.setGeometry(1250, 250, 500, 500)
        self.setWindowIcon(QIcon("C:\\Users\\pappm\\Pictures\\Saved Pictures\\wolf_icon.png"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #26ff00;"
                            "background-color: #1a1c1b;"
                            "font-weight: bold;")
        # label.setAlignment(Qt.AlignTop) # VERTICALLY TOP
        # label.setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM
        # label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER

        # label.setAlignment(Qt.AlignRight) # HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignHCenter) # HORIZONTALLY CENTER
        # label.setAlignment(Qt.AlignLeft) # HORIZONTALLY LEFT

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER AND TOP
        label.setAlignment(Qt.AlignCenter) # CENTER AND CENTER WITH SHORTCUT

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
