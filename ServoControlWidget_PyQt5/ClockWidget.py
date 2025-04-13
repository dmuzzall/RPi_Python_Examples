#!/usr/bin/env python

import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ClockWidget(QWidget):
    secSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.Setup_Layout()
        self.Setup_Timer()
        self.Update()

    def Setup_Layout(self):
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.dateTimeLabel = QLabel()
        self.dateTimeLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.layout.addWidget(self.dateTimeLabel)

    def Setup_Timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.Update)

        # Sync Clock to second
        curDateTime = QDateTime.currentDateTime()
        mSec = float(1000-int(curDateTime.toString("zzz")))
        time.sleep(mSec/1000)
        self.timer.start(1000)

    def Update(self):
        curDateTime = QDateTime.currentDateTime()
        curDateTimeStr = curDateTime.toString('yyyy-MM-dd  hh:mm:ss')
        self.dateTimeLabel.setText(curDateTimeStr)
        self.secSignal.emit()
