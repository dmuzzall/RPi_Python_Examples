from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Lib_GpioModule import Gpio_Input


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
        # state = GPIO.input(self.channel)
        state = Gpio_Input(self.channel)
        if state:
            style = f"color: white; background-color: green;"
        else:
            style = f"color: black; background-color: red;"
        self.channelLabel.setStyleSheet(style)


