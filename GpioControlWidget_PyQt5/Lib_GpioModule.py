import RPi.GPIO as GPIO


# Constant Values
GpioHI = GPIO.HIGH
GpioLO = GPIO.LOW
GpioIN = GPIO.IN
GpioOUT = GPIO.OUT

# Set GPIO Mode
GPIO.setmode(GPIO.BCM)  # Or GPIO.BOARD

# GPIO Methods
def Gpio_Setup(pin, mode):
    GPIO.setup(pin, mode)

def Set_Gpio_Output(pin, state):
    GPIO.output(pin, state)

def Get_Gpio_Input(pin):
    return GPIO.input(pin)

def Gpio_Cleanup():
    GPIO.cleanup()
