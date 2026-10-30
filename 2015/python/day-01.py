with open("../input/day-01.in") as file:
    input = file.readline()

def last_floor(directions):
    floor = 0

    for i, ch in enumerate(directions):
        floor = floor + 1 if ch == '(' else floor - 1
    
    return floor

for test in [
    ("(())", 0),
    ("()()", 0),
    ("(((", 3),
    ("(()(()(", 3),
    ("))(((((", 3),
    ("())", -1),
    ("))(", -1),
    (")))", -3),
    (")())())", -3),
]:
    assert last_floor(test[0]) == test[1]

def first_basement_index(directions):
    floor = 0
    basement_index = -1

    for i, ch in enumerate(directions):
        floor = floor + 1 if ch == '(' else floor - 1

        if basement_index == -1 and floor == -1:
            basement_index = (i + 1) # add one because input is 1-indexed

    return basement_index

for test in [
    (")", 1),
    ("()())", 5),
]:
    assert first_basement_index(test[0]) == test[1]

print("Part 1: " + str(last_floor(input)))
print("Part 2: " + str(first_basement_index(input)))