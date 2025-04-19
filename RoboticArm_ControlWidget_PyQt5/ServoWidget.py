from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PCA9685 import PCA9685
from Lib_LogFile import LogFile
from Lib_ColorWheel import *

class ServoWidget(QWidget):

    def __init__(self, channel: int, pwm: PCA9685, logFile: LogFile,
                 pwmMin: int, pwmMax: int, pwmValue: int):
        QWidget.__init__(self)
        self.channel = channel
        self.pwm = pwm
        self.logFile = logFile
        self.Set_PwmMin(pwmMin)
        self.Set_PwmMax(pwmMax)
        self.Setup_Layout()
        self.Setup_InfoLayout()
        self.Setup_Controls()
        self.Update_MinMax_SpinBoxes()
        self.Set_Value(pwmValue)

    def Setup_Layout(self):
        self.layout = QHBoxLayout()
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.setLayout(self.layout)

    def Setup_InfoLayout(self):
        self.infoLayout = QVBoxLayout()
        self.channelLabel = QLabel(str(self.channel))
        self.lcdNumber = QLCDNumber()
        self.channelLabel.setFont(QFont("Arial", 28))
        self.channelLabel.setAlignment(Qt.AlignCenter)
        self.channelLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        SetLabel_BackgroundColorWheel(self.channel, 16, self.channelLabel)
        self.infoLayout.addWidget(self.channelLabel)
        self.infoLayout.addWidget(self.lcdNumber)
        self.Setup_MinMaxLayout()
        self.layout.addLayout(self.infoLayout)

    def Setup_MinMaxLayout(self):
        self.minMaxLayout = QHBoxLayout()
        self.minSpinBox = QSpinBox()
        self.maxSpinBox = QSpinBox()
        self.minSpinBox.setRange(0,2000)
        self.maxSpinBox.setRange(1000,3000)
        self.minSpinBox.setValue(self.pwmMin)
        self.maxSpinBox.setValue(self.pwmMax)
        self.minMaxLayout.addWidget(self.minSpinBox)
        self.minMaxLayout.addWidget(self.maxSpinBox)
        self.infoLayout.addLayout(self.minMaxLayout)
        self.minSpinBox.valueChanged.connect(self.OnMinSpinBox_ValueChanged)
        self.maxSpinBox.valueChanged.connect(self.OnMaxSpinBox_ValueChanged)

    def Setup_Controls(self):
        self.controlsLayout = QVBoxLayout()
        self.dial = QDial()
        self.slider = QSlider()
        self.dial.setSingleStep(1)
        self.slider.setOrientation(Qt.Horizontal)
        self.controlsLayout.addWidget(self.dial)
        self.controlsLayout.addWidget(self.slider)
        self.layout.addLayout(self.controlsLayout)
        self.Reset_ControlRanges()
        self.dial.valueChanged.connect(self.OnDial_ValueChanged)
        self.slider.valueChanged.connect(self.OnSlider_ValueChanged)

    def OnMinSpinBox_ValueChanged(self):
        self.pwmMin = self.minSpinBox.value()
        self.Check_Value_MinMax()
        self.Reset_ControlRanges()

    def OnMaxSpinBox_ValueChanged(self):
        self.pwmMax = self.maxSpinBox.value()
        self.Check_Value_MinMax()
        self.Reset_ControlRanges()

    def OnDial_ValueChanged(self):
        value = self.dial.value()
        self.Set_Value(value)

    def OnSlider_ValueChanged(self):
        value = self.slider.value()
        self.Set_Value(value)

    def Check_Value_MinMax(self):
        if self.lcdNumber.intValue() < self.pwmMin:
            self.Set_Value(self.pwmMin)
        if self.lcdNumber.intValue() > self.pwmMax:
            self.Set_Value(self.pwmMax)

    def Reset_ControlRanges(self):
        self.dial.setRange(self.pwmMin, self.pwmMax)
        self.slider.setRange(self.pwmMin, self.pwmMax)

    def Get_Channel(self):
        return self.channel

    def Set_Value(self, value):
        if value is None:
            return
        if self.dial.value() != value:
            self.dial.setValue(value)
        if self.slider.value() != value:
            self.slider.setValue(value)
        self.lcdNumber.display(value)
        self.pwm.setServoPulse(self.channel, value)
        self.Log(f"{self.channel},{value}")
        self.lastValue = value

    def Get_Value(self):
        return self.lastValue

    def Set_PwmMin(self, pwmMin):
        if pwmMin is None:
            self.pwmMin = 500
        else:
            self.pwmMin = pwmMin

    def Update_MinMax_SpinBoxes(self):
        self.minSpinBox.setValue(self.pwmMin)
        self.maxSpinBox.setValue(self.pwmMax)

    def Get_PwmMin(self):
        return self.pwmMin

    def Set_PwmMax(self, pwmMax):
        if pwmMax is None:
            self.pwmMax = 2500
        else:
            self.pwmMax = pwmMax

    def Get_PwmMax(self):
        return self.pwmMax

    def Log(self, message: str):
        if self.logFile is not None:
            self.logFile.Log(message)
