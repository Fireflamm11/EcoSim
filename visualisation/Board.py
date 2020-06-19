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
            # window.columnconfigure((x, x + len(window.winfo_children())),
            #                        weight=1, minsize=50)
            # window.rowconfigure((x, x + len(window.winfo_children())),
            #                     weight=1, minsize=50)
            # window.columnconfigure(x, weight=1, minsize=50)
            # window.rowconfigure(x, weight=1, minsize=50)
            for y in range(world.grid.height):
                help_x = x * 2
                if y % 2 == 0:
                    if x == 0:
                        self.add_offset_row(x, y)
                    help_x += 1
                cell = PlaceFrame(master=self.window, relief=tk.RAISED,
                                  borderwidth=5)
                self.world.grid.places[x][y].add_observer(cell)
                tk.Label(cell, text=str(x) + ", " + str(y)).pack(fill=tk.BOTH)
                cell.grid(row=y * 2, column=help_x, padx=5, pady=5,
                          sticky="nesw", rowspan=2, columnspan=2)

        for col_num in range(window.grid_size()[1]):
            window.columnconfigure(col_num, weight=1, minsize=50)
        for row_num in range(window.grid_size()[0]):
            window.rowconfigure(row_num, weight=1, minsize=50)

    def add_offset_row(self, x, y):
        cell = tk.Frame(master=self.window)
        cell.grid(row=y * 2, column=x, sticky="nesw", rowspan=2, columnspan=1)

    def step(self):
        pass
