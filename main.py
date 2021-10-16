from PyQt5.QtWidgets import QMainWindow, QApplication
import test_ui
import sys


class testGUI(QMainWindow, test_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    gui = testGUI()

    gui.show()
    app.exec_()

if __name__ == '__main__':
    main()


