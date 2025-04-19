import datetime as datetime

class LogFile():

    def __init__(self, fileName='', printToScreenFlag=True, appendFlag=True):
        super().__init__()
        self.printToScreenFlag = printToScreenFlag
        self.appendFlag = appendFlag
        self.Set_FileName(fileName)
        self.Open()

    def Set_FileName(self, fileName):
        if fileName == '':
            dateStr = datetime.date.today().strftime("%Y%m%d")
            self.fileName = "{0}_logFile.csv".format(dateStr)
        else:
            self.fileName = fileName

    def Open(self):
        mode = 'a' if self.appendFlag else 'w'
        self.logFile = open(self.fileName, mode)

    def Get_DateTimeStr(self):
        now = datetime.datetime.now()
        return now.strftime("%Y%m%d_%H%M%S.%f")[:-3]

    def Log(self, logLine):
        if self.logFile:
            formatLine = f"{self.Get_DateTimeStr()} {logLine}\n"
            self.logFile.write(formatLine)
            self.logFile.flush()
        if self.printToScreenFlag:
            print(logLine)

    def Close(self):
        self.logFile.close()
