from cell import Cell


class Spreadsheet:
    def __init__(self, row: int, column: int):
        self.__cells = []
        self.__make_sheet(row, column)

    def get_cells(self):
        return self.__cells

    def __make_sheet(self, row: int, column: int) -> None:
        for i in range(row):
            self.__cells.append([""] * column)

    def set_cell_at(self, row: int, column: int, value: str) -> None:
        self.__cells[row][column] = Cell(value)

    def get_cell_at(self, row: int, column: int) -> Cell:
        return self.__cells[row][column]

    def add_row(self, index_row: int) -> None:
        self.__cells.insert(index_row, [""] * len(self.__cells[0]))

    def remove_row(self, index_row: int) -> None:
        self.__cells.pop(index_row-1)

    def add_column(self, index_col: int) -> None:
        for row in self.__cells:
            row.insert(index_col, [""])

    def remove_column(self, index_col: int) -> None:
        for row in self.__cells:
            row.pop(index_col-1)

    def swap_rows(self, first_row: int, second_row: int) -> None:
        self.__cells[first_row-1], self.__cells[second_row-1] = \
            self.__cells[second_row-1], self.__cells[first_row-1]

    def swap_columns(self, first_col: int, second_col: int) -> None:
        for row in self.__cells:
            self.__cells[row][first_col-1], self.__cells[row][second_col-1] = \
                self.__cells[row][second_col-1], self.__cells[row][first_col-1]
