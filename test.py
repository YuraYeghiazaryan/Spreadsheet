from cell import Cell
from spreadsheet import Spreadsheet
from datetime import datetime
from config import *


def show_result(func, value, func_name):
    if func == value:
        print(func_name, ' function  passed')
    else:
        print(func_name, ' function failed')


# for class Cell
def test_set_get_value(value: str):
    cell = Cell(value)
    show_result(cell.get_value(), value, "Cell.set_value() and Cell.get_value()")


def test_set_get_color(color):
    cell = Cell('34')
    cell.set_color(color)
    show_result(cell.get_color(), colors[color], "Cell.set_color() and Cell.get_color()")


def test_to_int(value):
    cell = Cell(value)
    show_result(type(cell.to_int()), int, "Cell.to_int()")


def test_to_float(value):
    cell = Cell(value)
    cell.to_float()
    show_result(type(cell.to_float()), float, "Cell.to_float()")


def test_to_date(value):
    cell = Cell(value)
    cell.to_date()
    show_result(type(cell.to_date()), datetime, "Cell.to_date()")


def test_reset(value):
    cell = Cell(value)
    cell.reset()
    show_result(cell.get_value(), "", "Cell.reset()")


# for class Spreadsheet

def test_make_sheet(row: int, col: int):
    sheet = Spreadsheet(row, col)
    show_result(shape(sheet.get_cells()), (row, col), "Spreadsheet.make_sheet()")


def shape(arr: list):
    row = len(arr)
    col = len(arr[0])
    return row, col


def test_set_cell_at(row: int, col: int, value):
    sheet = Spreadsheet(row+3, col+3)
    sheet.set_cell_at(row, col, value)
    show_result(sheet.get_cells()[row][col].get_value(), value, "Spreadsheet.set_cell_at()")


def test_get_cell_at(row, col):
    sheet = Spreadsheet(row+4, col+4)
    sheet.set_cell_at(row, col, "78")
    show_result(sheet.get_cell_at(row, col), sheet.get_cells()[row][col], "Spreadsheet.get_cell_at()")


def test_add_row(row, col, index_row):
    sheet = Spreadsheet(row + 4, col + 4)
    before_size_of_row = len(sheet.get_cells())
    sheet.add_row(index_row)
    show_result(len(sheet.get_cells()) - before_size_of_row, 1, "Spreadsheet.add_row()")


def test_remove_row(row, col, index_row):
    sheet = Spreadsheet(row, col)
    before_count_of_row = len(sheet.get_cells())
    sheet.remove_row(index_row)
    show_result(before_count_of_row - len(sheet.get_cells()), 1, "Spreadsheet.remove_row()")


def test_add_column(row, col, index_col):
    sheet = Spreadsheet(row, col)
    before_count_of_col = len(sheet.get_cells()[0])
    sheet.add_column(index_col)
    show_result(len(sheet.get_cells()[0]) - before_count_of_col, 1, "Spreadsheet.add_column()")


def test_remove_column(row, col, index_col):
    sheet = Spreadsheet(row, col)
    before_count_of_col = len(sheet.get_cells()[0])
    sheet.remove_column(index_col)
    show_result(before_count_of_col - len(sheet.get_cells()[0]), 1, "Spreadsheet.remove_column()")


def test_swap_rows(row, col, row1, row2):
    sheet = Spreadsheet(row, col)
    sheet.swap_rows(row1, row2)
    before = (sheet.get_cells()[row1-1], sheet.get_cells()[row2-1])
    show_result((sheet.get_cells()[row1-1], sheet.get_cells()[row2-1]), before, "Spreadsheet.swap_rows()")


def test_swap_columns(row, col, col1, col2):
    sheet = Spreadsheet(row, col)
    before_col1 = [item[col1-1] for item in sheet.get_cells()]
    before_col2 = [item[col2-1] for item in sheet.get_cells()]
    sheet.swap_columns(col1, col2)
    after_col1 = [item[col1-1] for item in sheet.get_cells()]
    after_col2 = [item[col2-1] for item in sheet.get_cells()]
    before = (before_col1, before_col2)
    after = (after_col1, after_col2)
    show_result(after, before, "Spreadsheet.swap_columns()")


test_set_get_value("34")
test_set_get_color(4)
test_to_int("44")
test_to_float("43")
test_to_date("2022-09-11")
test_reset("324")

test_make_sheet(4, 3)
test_set_cell_at(5, 3, "88")
test_get_cell_at(3, 2)
test_add_row(4, 3, 2)
test_remove_row(4, 5, 3)
test_add_column(5, 4, 2)
test_remove_column(4, 2, 1)
test_swap_rows(5, 5, 2, 4)
test_swap_columns(6, 8, 3, 4)



