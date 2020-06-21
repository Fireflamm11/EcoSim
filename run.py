import tkinter as tk

from implementation.print_world import print_world
from structure.World import World
from visualisation.Board import Board

root = tk.Tk()


def clear_window():
    for child in root.winfo_children():
        child.destroy()


def print_test():
    clear_window()
    print_world()


def test_world():
    clear_window()
    world = World(20, 20, 'test_agriculture')
    board = Board(world, root)

    def step():
        print('Date: ', world.date)
        world.step()
        board.step()
        print('Dead People: ', len(world.dead_pops))
        root.after(100, step)

    step()


if __name__ == '__main__':
    test_world()

root.mainloop()

