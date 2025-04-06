import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import RPi.GPIO as GPIO
from Lib_LogFile import LogFile

GPIO.setmode(GPIO.BCM)


class GpioControl():
    def __init__(self):
        self.gpioList = []
        self.Setup_LogFile()
        self.Log("GpioControl started")
    def __del__(self):
        print("GpioControl Cleanup")
        self.logFile.Close()
        GPIO.cleanup()

    def Setup_LogFile(self):
        self.logFile = LogFile('log.csv', True, False)

    def Log(self, message: str):
        self.logFile.Log(message)

    def Add_Gpio(self, channel: int):
        if channel in self.gpioList:
            self.Log(f"GpioControl Add_Gpio: Already Added: {channel}")
        else:
            GPIO.setup(channel, GPIO.OUT)
            self.gpioList.append(channel)
            self.Log(f"GpioControl Add_Gpio: {channel}")

    def Set_Gpio(self, channel: int, state: bool):
        if channel not in self.gpioList:
            self.Log(f"GpioControl Set_Gpio: {channel} not added")
            return
        if state:
            GPIO.output(channel, GPIO.HIGH)
        else:
            GPIO.output(channel, GPIO.LOW)
            self.Log(f"Set_Gpio {channel} {state}")

    def Toggle_Gpio(self, channel: int):
        state = GPIO.input(channel)
        GPIO.output(channel, not state)
        self.Log(f"Toggle_Gpio {channel} {int(state)} -> {int(not state)}")
        

class GpioWidget(QWidget):
    def __init__(self, channel, gpioControl):
        super().__init__()
        self.gpioControl = gpioControl
        self.channel = channel
        self.Setup_Layout()
        self.Update_LabelColor()

    def Setup_Layout(self):
        self.layout = QHBoxLayout()
        self.channelLabel = QLabel()
        self.button = QPushButton()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.channelLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.channelLabel.setFixedWidth(30)
        self.channelLabel.setFixedHeight(22)
        self.channelLabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.channelLabel)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.channelLabel.setText(str(self.channel))
        self.button.clicked.connect(self.OnButton_clicked)

    def OnButton_clicked(self):
        self.gpioControl.Toggle_Gpio(self.channel)
        self.Update_LabelColor()

    def Update_LabelColor(self):
        state = GPIO.input(self.channel)
        if state:
            style = f"color: white; background-color: green;"
        else:
            style = f"color: black; background-color: red;"
        self.channelLabel.setStyleSheet(style)


class GpioControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.gpioWidgetList = []
        self.Setup_Layout()
        self.Setup_Gpio()

    def Setup_Layout(self):
        self.layout = QVBoxLayout()
        self.gpioGroupBoxLayout = QVBoxLayout()
        self.gpioWidgetGroupBox = QGroupBox("Gpio Control Widget")
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.gpioGroupBoxLayout.setSpacing(0)
        self.gpioGroupBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.gpioWidgetGroupBox.setLayout(self.gpioGroupBoxLayout)
        self.layout.addWidget(self.gpioWidgetGroupBox)
        self.setLayout(self.layout)

    def Setup_Gpio(self):
        self.gpioControl = GpioControl()

    def Add_GpioWidget(self, channel: int):
        self.gpioControl.Add_Gpio(channel)
        gpioWidget = GpioWidget(channel, self.gpioControl)
        self.gpioWidgetList.append(gpioWidget)
        self.gpioGroupBoxLayout.addWidget(gpioWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GpioControlWidget()
    w.Add_GpioWidget(18)
    w.Add_GpioWidget(23)
    w.Add_GpioWidget(24)
    w.Add_GpioWidget(25)
    w.show()
    exit_code = app.exec_()
    sys.exit(exit_code)
