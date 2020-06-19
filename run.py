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
    world = World(5, 5, 'test_food')
    board = Board(world, window)

    def step():
        print(world.date)
        world.step()
        board.step()
        window.after(200, step)

    step()



if __name__ == '__main__':
    button = tk.Button(window, text='print', width=25, command=print_test)
    button.grid()
    button = tk.Button(window, text='food', width=25, command=test_world)
    button.grid()
    window.mainloop()
