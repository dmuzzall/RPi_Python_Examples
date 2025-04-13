from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PCA9685 import PCA9685


class ServoWidget(QWidget):

    def __init__(self, channel: int, pwm: PCA9685):
        QWidget.__init__(self)
        self.channel = channel
        self.pwm = pwm
        self.pwmMin = 750
        self.pwmMax = 2500
        self.Setup_Layout()
        self.Setup_Dial()
        self.Setup_Slider()
        self.Setup_LcdNumber()

    def Setup_Layout(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.setLayout(self.layout)

    def Setup_Dial(self):
        self.dial = QDial()
        self.dial.setRange(self.pwmMin, self.pwmMax)
        self.dial.setSingleStep(1)
        self.layout.addWidget(self.dial)
        self.dial.valueChanged.connect(self.OnDial_ValueChanged)

    def Setup_Slider(self):
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setRange(self.pwmMin, self.pwmMax)
        self.layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.OnSlider_ValueChanged)

    def Setup_LcdNumber(self):
        self.lcdNumber = QLCDNumber()
        self.lcdNumber.setMinimumHeight(40)
        self.layout.addWidget(self.lcdNumber)

    def OnDial_ValueChanged(self):
        print('OnDial_ValueChanged')
        value = self.dial.value()
        self.Set_Value(value)

    def OnSlider_ValueChanged(self):
        print('OnSlider_ValueChanged')
        value = self.slider.value()
        self.Set_Value(value)

    def Set_Value(self, value):
        if self.dial.value() != value:
            self.dial.setValue(value)
        if self.slider.value() != value:
            self.slider.setValue(value)
        self.lcdNumber.display(value)
        self.pwm.setServoPulse(self.channel, value)
