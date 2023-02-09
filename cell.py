from config import *
from datetime import date


class Cell:
    def __init__(self, value: str):
        self.__value = value
        self.__color = colors[5]

    def set_value(self, value: str):
        self.__value = str(value)

    def set_color(self, color):
        if color in colors:
            self.__color = colors[color]
        else:
            return "Color not found "

    def get_value(self):
        return self.__value

    def get_color(self):
        return self.__color

    def to_int(self):
        return int(self.__value)

    def to_float(self):
        return float(self.__value)

    def to_date(self):
        try:
            date(int(self.__value[:4]), int(self.__value[5:7], int(self.__value[8:])))
        except:
            "cannot be converted to date"

    def reset(self):
        self.__value = ''
