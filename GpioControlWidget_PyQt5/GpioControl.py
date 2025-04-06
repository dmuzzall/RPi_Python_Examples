from Lib_GpioModule import Gpio_Setup, Gpio_Output, Gpio_Input, Gpio_Cleanup
from Lib_GpioModule import GpioHI, GpioLO, GpioIN, GpioOUT
from Lib_LogFile import LogFile


class GpioControl():

    def __init__(self):
        self.gpioList = []
        self.Setup_LogFile()
        self.Log("GpioControl started")

    def __del__(self):
        print("GpioControl Cleanup")
        self.logFile.Close()
        Gpio_Cleanup()

    def Setup_LogFile(self):
        self.logFile = LogFile('log.csv', True, False)

    def Log(self, message: str):
        self.logFile.Log(message)

    def Add_Gpio(self, pin: int):
        if pin in self.gpioList:
            self.Log(f"GpioControl Add_Gpio: Already Added: {pin}")
        else:
            Gpio_Setup(pin, GpioOUT)
            self.gpioList.append(pin)
            self.Log(f"GpioControl Add_Gpio: {pin}")

    def Set_GpioState(self, pin: int, state: bool):
        if pin not in self.gpioList:
            self.Log(f"GpioControl Set_Gpio: {pin} not added")
            return
        if state:
            Gpio_Output(pin, GpioHI)
        else:
            Gpio_Output(pin, GpioLO)

    def Toggle_Gpio(self, pin: int):
        state = Gpio_Input(pin)
        Gpio_Output(pin, not state)
        self.Log(f"Toggle_Gpio {pin} {int(state)} -> {int(not state)}")

    def Get_GpioState(self, pin: int):
        state = Gpio_Input(pin)
        return state


# # Unit Test
# import time
# gc = GpioControl()
# pin = 18
# gc.Add_Gpio(pin)
# print(f"{pin} Set_Gpio True")
# gc.Set_GpioState(pin, True)
# time.sleep(2)
# print(f"{pin} Set_Gpio False")
# gc.Set_GpioState(pin, False)
# time.sleep(2)
