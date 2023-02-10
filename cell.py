import datetime
from config import *


class Cell:
    def __init__(self, value: str):
        self.__value = value
        self.__color = colors[5]

    def set_value(self, value: str):
        self.__value = str(value)

    def set_color(self, color):
        if color not in colors:
            raise ValueError(f'There is no such a color: {color}.')

        self.__color = colors[color]

    def get_value(self):
        return self.__value

    def get_color(self):
        return self.__color

    def to_int(self):
        return int(self.__value)

    def to_float(self):
        return float(self.__value)

    def to_date(self):
        return datetime.datetime.strptime(self.__value, "%Y-%m-%d")

    def reset(self):
        self.__value = ''
