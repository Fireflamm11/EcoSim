from structure.World import World
from implementation.print_world import print_world


def print_test():
    print_world()


def test_world():
    world = World(50, 50, 'test_food')
    for x in range(50):
        world.step()


if __name__ == '__main__':
    print_test()
