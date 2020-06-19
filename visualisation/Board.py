import tkinter as tk

from visualisation.PlaceFrame import PlaceFrame

"""
Inspired by/Using:
https://github.com/noobien/pytk-hexagon-grid/blob/master/hexagon.py
https://stackoverflow.com/questions/26583602/displaying-data-in-a-hexagonal-grid-using-python
for hexagon-grid
"""


class Board:

    def __init__(self, world, window):
        self.world = world
        self.window = window

        for x in range(world.grid.width):
            for y in range(world.grid.height):
                help_x = x * 2
                if y % 2 == 0:
                    help_x += 1

                cell = PlaceFrame(master=self.window, relief=tk.RAISED,
                                  borderwidth=5)
                self.world.grid.places[x][y].add_observer(cell)
                tk.Label(cell, text=0).pack(fill=tk.BOTH)
                cell.grid(row=y * 2, column=help_x, padx=5, pady=5,
                          sticky="nesw", rowspan=2, columnspan=2)

        for y in range(world.grid.height):
            if y % 2 == 1:
                cell = tk.Frame(master=self.window)
                cell.grid(row=y * 2, column=world.grid.width * 2,
                          sticky="nesw")

        for col_num in range(window.grid_size()[1] + 1):
            window.columnconfigure(col_num, weight=1, minsize=50)
        for row_num in range(window.grid_size()[0]):
            window.rowconfigure(row_num, weight=1, minsize=50)

    def add_offset_row(self, x, y):
        cell = tk.Frame(master=self.window, bg='blue')
        cell.grid(row=y * 2, column=2 * x, sticky="nesw", rowspan=2,
                  columnspan=2, padx=5, pady=5)

    def step(self):
        pass
