from PyQt5.QtWidgets import *
from GpioControl import GpioControl
from GpioWidget import GpioWidget


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
