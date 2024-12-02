def calculate_water_units(container):
    units = 0
    wall = 0
    next_wall = 0

    for index, blocks in enumerate(container):
        if blocks < 0:
            continue

        if index != len(container) - 1 and (index == 0 or next_wall == blocks):
            wall = blocks if index == 0 else next_wall
            next_wall = 0
            for next_blocks_index in range(index + 1, len(container)):
                if container[next_blocks_index] >= next_wall and wall >= next_wall:
                    next_wall = container[next_blocks_index]
        else:
            reference_wall = wall if next_wall > wall else next_wall
            current_blocks = reference_wall - blocks
            units += current_blocks if current_blocks >= 0 else 0

    return units


print(calculate_water_units([4, 0, 3, 6]))
print(calculate_water_units([4, 0, 3, 6, 1, 3]))
print(calculate_water_units([5, 4, 3, 2, 1, 0]))
print(calculate_water_units([0, 1, 2, 3, 4, 5]))
print(calculate_water_units([4, 0, 3, 6, 1, 3, 0, 1, 6]))
