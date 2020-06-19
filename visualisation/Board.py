from tkinter import *


class Board:

    def __init__(self, world, window):
        self.world = world
        self.window = window

        layout = []
        for x in range(world.grid.width):
            layout.append([])
            for y in range(world.grid.height):
                cell = Label(self.window, text=str(x) + " " + str(y),
                             background='blue')
                cell.grid(row=y, column=x)
                layout[x].append(cell)
        self.draw_board()

    def draw_board(self):
        pass

    def step(self):
        pass
