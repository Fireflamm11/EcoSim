import tkinter as tk

from implementation.print_world import print_world
from structure.World import World
from visualisation.Board import Board

window = tk.Tk()


def clear_window():
    for child in window.winfo_children():
        child.destroy()


def print_test():
    clear_window()
    print_world()


def test_world():
    clear_window()
    world = World(25, 25, 'test_agriculture')
    board = Board(world, window)

    def step():
        print('Date: ', world.date)
        world.step()
        board.step()
        print('Dead People: ', len(world.dead_pops))
        window.after(200, step)

    step()


if __name__ == '__main__':
    test_world()

window.mainloop()

