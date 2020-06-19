from structure.World import World


def print_world():
    world = World(3, 3)

    directions = ['nw', 'ne', 'e', 'se', 'sw', 'w']
    print('x-Coordinate')
    x = int(input())
    print('y-Coordinate')
    y = int(input())

    try:
        place = world.grid.places[x][y]
    except IndexError:
        if x >= len(world.grid.places):
            x = x - len(world.grid.places)
        if y >= len(world.grid.places[x]):
            y = y - len(world.grid.places[x])
        place = world.grid.places[x][y]

    for direction in directions:
        neighbor = place.get_neighbor(direction)
        print(direction + ': ', neighbor.x, neighbor.y)
