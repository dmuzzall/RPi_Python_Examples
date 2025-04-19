import sys
from PyQt5.QtWidgets import QApplication
from ServoControlWidget import ServoControlWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Oxygen')  # 'Fusion', 'Motif' 'Breeze', 'Oxygen', 'QtCurve', 'Windows'
    w = ServoControlWidget()
    w.show()
    sys.exit(app.exec_())
