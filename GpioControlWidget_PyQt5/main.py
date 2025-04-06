import sys
from PyQt5.QtWidgets import *
from GpioControlWidget import GpioControlWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GpioControlWidget()

    w.Add_GpioWidget(18)
    w.Add_GpioWidget(23)
    w.Add_GpioWidget(24)
    w.Add_GpioWidget(25)

    w.show()
    sys.exit(app.exec_())
