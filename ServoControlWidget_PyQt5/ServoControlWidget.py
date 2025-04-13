import sys
from PyQt5.QtWidgets import *
from PCA9685 import PCA9685
from ClockWidget import ClockWidget
from ServoWidget import ServoWidget


class ServoControlWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.setLayout(self.layout)
        self.Setup_Servo()
        # self.Setup_ClockWidget()
        self.Setup_ServoWidget()

    def Setup_Servo(self):
        self.pwm = PCA9685(0x40, debug=False)
        self.pwm.setPWMFreq(50)

    def Setup_ClockWidget(self):
        self.clockWidget = ClockWidget()
        self.layout.addWidget(self.clockWidget)
        self.clockWidget.secSignal.connect(self.OnSecSignal)

    def Setup_ServoWidget(self):
        channel = 0
        self.servoWidget = ServoWidget(channel, self.pwm)
        self.layout.addWidget(self.servoWidget)

    def OnSecSignal(self):
        print("OnSecSignal")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Oxygen')  # 'Fusion', 'Motif' 'Breeze', 'Oxygen', 'QtCurve', 'Windows'
    w = ServoControlWidget()
    w.show()
    sys.exit(app.exec_())
