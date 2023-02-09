from cell import Cell
from spreadsheet import Spreadsheet
from datetime import date

sh = Spreadsheet(4, 5)


def show_result(func, value):
    if func == value:
        print(f'{func} function  passed')
    else:
        print(f'{func} function failed')


# for class Cell
def test_set_get_value(value: str):
    cell = Cell(value)
    show_result(cell.get_value(), value)


def test_set_get_color(color):
    cell = Cell('34')
    cell.set_color(color)
    show_result(cell.get_color(), color)


def test_to_int(value):
    cell = Cell(value)
    show_result(type(cell.to_int()), int)


def test_to_float(value):
    cell = Cell(value)
    cell.to_float()
    show_result(type(cell.to_float()), float)


def test_to_date(value):
    cell = Cell(value)
    cell.to_date()
    show_result(type(cell.get_value()), date)
