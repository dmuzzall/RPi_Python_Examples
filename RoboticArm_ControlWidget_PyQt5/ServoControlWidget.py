import pandas as pd
from PCA9685 import PCA9685
from PyQt5.QtWidgets import *
from Lib_LogFile import LogFile
from ServoWidget import ServoWidget


class ServoControlWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.Setup_Layout()
        self.Setup_LogFile()
        self.Setup_PWM()
        self.Setup_Controls()

        self.Load_ConfigFile()
        self.Setup_ServoWidgets()

    def Setup_Layout(self):
        self.layout = QGridLayout()
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.setLayout(self.layout)

    def Setup_LogFile(self):
        self.logFile = LogFile('log.csv', True, False)

    def Setup_PWM(self):
        self.pwm = PCA9685(0x40, debug=False)
        self.pwm.setPWMFreq(50)

    def Setup_Controls(self):
        self.saveButton = QPushButton('Save')
        self.loadbutton = QPushButton('Load')
        self.layout.addWidget(self.saveButton, 0, 0)
        self.layout.addWidget(self.loadbutton, 0, 1)
        self.saveButton.clicked.connect(self.OnSaveButton_Clicked)
        self.loadbutton.clicked.connect(self.OnLoadButton_Clicked)

    def Setup_ServoWidgets(self):
        self.servoWidgetDict = {}
        self.Add_ServoWidget(0, 1, 0)
        self.Add_ServoWidget(2, 1, 1)
        self.Add_ServoWidget(4, 1, 2)
        self.Add_ServoWidget(6, 2, 0)
        self.Add_ServoWidget(8, 2, 1)
        self.Add_ServoWidget(10, 2, 2)

    def Add_ServoWidget(self, channel, row, col):
        pwmMin = self.Find_ConfigValue(channel, 'Min')
        pwmMax = self.Find_ConfigValue(channel, 'Max')
        pwmValue = self.Find_ConfigValue(channel, 'Value')
        print(f"Add_ServoWidget {pwmMin} {pwmMax} {pwmValue}")
        servoWidget = ServoWidget(channel, self.pwm, self.logFile, pwmMin, pwmMax, pwmValue)
        self.servoWidgetDict[channel] = servoWidget
        self.layout.addWidget(servoWidget, row, col)

    def Save_ConfigFile(self):
        with open("config.csv", "w") as configFile:
            for channel in self.servoWidgetDict:
                servoWidget = self.servoWidgetDict[channel]
                line = (f"{channel},{servoWidget.Get_PwmMin()},"
                        f"{servoWidget.Get_PwmMax()},{servoWidget.Get_Value()}")
                print(line)
                configFile.write(line + '\n')

    def Load_ConfigFile(self):
        self.configDf = pd.read_csv('config.csv', header=None)
        self.configDf.columns = ['Channel', 'Min', 'Max', 'Value']
        print("Load_ConfigFile")
        print(self.configDf.to_string(index=False))

    def Find_ConfigValue(self, channel, col):
        try:
            val = self.configDf.loc[self.configDf['Channel'] == channel, col].values[0]
            return val
        except:
            return None

    def Log(self, message: str):
        self.logFile.Log(message)

    def OnSaveButton_Clicked(self):
        print("OnSaveButton_Clicked")
        self.Save_ConfigFile()

    def OnLoadButton_Clicked(self):
        print("OnLoadButton_Clicked")
        self.Load_ConfigFile()
