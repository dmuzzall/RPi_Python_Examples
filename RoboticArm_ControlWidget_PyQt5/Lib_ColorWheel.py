import math
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QLabel

def Get_Color_RBG(n: int, nMax: int):
    range = 255
    # Red
    rAngle = n / nMax * 2 * math.pi
    r = math.cos(rAngle)
    r = int((r + 1) / 2 * range)
    # Blue
    bAngle = rAngle + 2 * math.pi / 3
    b = math.cos(bAngle)
    b = int((b + 1) / 2 * range)
    # Green
    gAngle = bAngle + 2 * math.pi / 3
    g = math.cos(gAngle)
    g = int((g + 1) / 2 * range)
    # print(f"{r} {b} {g}")
    return QColor(r, g, b)

def SetLabel_BackgroundColorWheel(n: int, nMax: int, label: QLabel):
    c = Get_Color_RBG(n, nMax)
    label.setStyleSheet(f"background-color: rgb({c.red()}, {c.green()}, {c.blue()});")

# c0 = Get_Color_RBG(0, 3)
# print(c0)
# c1 = Get_Color_RBG(1, 3)
# print(c1)
# c2 = Get_Color_RBG(2, 3)
# print(c2)
