import copy

def is_in_universe(u_size, x, y, z):
    return (u_size > x > -u_size) and (u_size > y > -u_size) and (u_size > z > -u_size)


def count_active_neighbours(cubes, x, y, z):
    active = 0
    for z_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            for x_offset in range(-1, 2):
                if is_in_universe(universe_size, x + x_offset, y + y_offset, z + z_offset) and not (
                    x_offset == y_offset == z_offset == 0
                ):
                    cube = cubes[(x + x_offset, y + y_offset, z + z_offset)]
                    if cube == "#":
                        active += 1
                # else:
                # print("coordinates " + str(x+xinc), str(y+yinc), str(z+zinc) + " not valid", sep=',')
    return active


def print_cubes(cubes, x_layer, y_layer, z_layer):
    for z in range(-z_layer, z_layer + 1):
        print("\nz : " + str(z))
        for y in range(-y_layer, y_layer):
            for x in range(-x_layer, x_layer):
                print(cubes[(x, y, z)], end="")
            print()


def initiate_universe(cubes, data, size):
    for z in range(-size, size + 1):
        for y in range(-size, size + 1):
            for x in range(-size, size + 1):
                cubes[(x, y, z)] = "."

    for y, line in enumerate(data):
        for x, cube in enumerate(line):
            cubes[(x, y, 0)] = cube
    return cubes


def solve(cubes, nb_cycles, u_size):
    new_cubes = copy.deepcopy(cubes)
    for _ in range(nb_cycles):
        print_cubes(cubes, 20, 20, 1)
        cubes = copy.deepcopy(new_cubes)
        for z in range(-u_size, u_size):
            for y in range(-u_size, u_size):
                for x in range(-u_size, u_size):
                    active = count_active_neighbours(cubes, x, y, z)

                    if cubes[(x, y, z)] == "#" and active != 2 and active != 3:
                        new_cubes[(x, y, z)] = "."
                    elif cubes[(x, y, z)] == "." and active == 3:
                        new_cubes[(x, y, z)] == "#"
    return new_cubes


if __name__ == "__main__":
    with open( "day17_input" ) as f:
        data = f.read().split( "\n" )

    universe_size = 20
    nb_cycles = 6
    cubes = dict()
    cubes = initiate_universe(cubes, data, universe_size)

    cubes = solve(cubes, nb_cycles, universe_size)
    active = sum(value == "#" for value in cubes.values())

    print("After 6 cycles, " + str(active) + " remain active")
