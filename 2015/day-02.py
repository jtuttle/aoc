from functools import reduce

with open("day-02.in") as file:
    input = file.readlines()

def paper_total(dimensions):
    paper = 0

    for dim in dimensions:
        l,w,h = map(lambda x: int(x), dim.split('x'))
        areas = [l*w, w*h, h*l]
        paper += 2 * sum(areas) + min(areas)

    return paper

for test in [
    (["2x3x4"], 58),
    (["1x1x10"], 43),
]:
    assert paper_total(test[0]) == test[1]

def ribbon_total(dimensions):
    ribbon = 0

    for dim in dimensions:
        l,w,h = map(lambda x: int(x), dim.split('x'))
        sorted = [l,w,h]
        sorted.sort()

        ribbon += 2 * sorted[0] + 2 * sorted[1] + reduce(lambda x, y: x * y, sorted)

    return ribbon

for test in [
    (["2x3x4"], 34),
    (["1x1x10"], 14),
]:
    assert ribbon_total(test[0]) == test[1]

print("Part 1: " + str(paper_total(input)))
print("Part 2: " + str(ribbon_total(input)))