with open("../input/day-03.in") as file:
    input = file.readline()

def next_coord(coord, move):
    if move == ">":
        return (coord[0] + 1, coord[1])
    elif move == "<":
        return (coord[0] - 1, coord[1])
    elif move == "^":
        return (coord[0], coord[1] + 1)
    elif move == "v":
        return (coord[0], coord[1] - 1)
    else:
        raise Exception("invalid move")

def unique_house_count(directions, agent_count):
    agent_coords = [(0, 0)] * agent_count
    agent_index = 0
    visited = { (0, 0) }
    
    for ch in directions:
        coord = next_coord(agent_coords[agent_index], ch)
        agent_coords[agent_index] = coord
        visited.add(coord)

        agent_index = (agent_index + 1) % agent_count

    return len(visited)

for test in [
    (">", 1, 2),
    ("^>v<", 1, 4),
    ("^v^v^v^v^v", 1, 2),
    ("^v", 2, 3),
    ("^>v<", 2, 3),
    ("^v^v^v^v^v", 2, 11),
]:
    assert unique_house_count(test[0], test[1]) == test[2]

print("Part 1: " + str(unique_house_count(input, 1)))
print("Part 2: " + str(unique_house_count(input, 2)))