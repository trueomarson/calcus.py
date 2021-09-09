import sys

from PyQt5.Core import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

__version__ = '0.1'

class PyCalcUi(QMainWindow):

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
    
    def __init__(self):
        
        super().__init__()
       
        self.setWindowTitle('Calcus')
        self.setFixedSize(240, 240)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createDisplay()
        self._createButtons()


def main():
    calcus = QApplication(sys.argv)
    view = PyCalcUi()
    view.show()
    sys.exit(calcus.exec_())

if __name__ == '__main__':
    main()