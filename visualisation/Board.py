import tkinter as tk

from visualisation.PlaceFrame import PlaceFrame


class Board:

    def __init__(self, world, window):
        self.world = world
        self.window = window

        layout = []
        for x in range(world.grid.width):
            layout.append([])
            window.columnconfigure(x, weight=1, minsize=100)
            window.rowconfigure(x, weight=1, minsize=100)
            for y in range(world.grid.height):
                cell = PlaceFrame(master=self.window,
                                  relief=tk.RAISED, borderwidth=5)
                self.world.grid.places[x][y].add_observer(cell)
                tk.Label(cell,
                         text=str(x) + " " + str(y)).pack(fill=tk.BOTH)
                cell.grid(row=y, column=x, padx=5, pady=5, sticky="nesw")
                layout[x].append(cell)
        self.draw_board()

    def draw_board(self):
        pass

    def step(self):
        pass
