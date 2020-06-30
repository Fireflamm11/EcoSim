import tkinter as tk

from implementation.print_world import print_world
from structure.World import World
from visualisation.Board import Board

root = tk.Tk()
# root.geometry("{0}x{0}+0+0".format(
#             root.winfo_screenwidth(), root.winfo_screenheight()-50))
root.state('zoomed')


def clear_window():
    for child in root.winfo_children():
        child.destroy()


def print_test():
    clear_window()
    print_world()


def test_world():
    clear_window()
    world = World(4, 4, 'test_agriculture')
    board = Board(world, root)

    def step():
        print('##############################################################')
        print('Date: ', world.date)
        print('##############################################################')
        world.step()
        board.step()
        # print('Dead People: ', len(world.dead_pops))
        root.after(50, step)

    step()


if __name__ == '__main__':
    test_world()
    # print_test()

root.mainloop()
