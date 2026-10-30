with open("../input/day-05.in") as file:
    input = file.readlines()

VOWELS = {'a', 'e', 'i', 'o', 'u'}
BANNED = {"ab", "cd", "pq", "xy"}

def is_nice_1(str):
    vowel_count = 0
    has_repeat = False

    for i in range(len(str)):
        if str[i] in VOWELS:
            vowel_count += 1

        if i < len(str) - 1:
            if str[i] + str[i+1] in BANNED:
                return False

            if str[i] == str[i+1]:
                has_repeat = True

    return vowel_count >= 3 and has_repeat

for test in [
    ("ugknbfddgicrmopn", True),
    ("aaa", True),
    ("jchzalrnumimnmhp", False),
    ("haegwjzuvuyypxyu", False),
    ("dvszwmarrgswjxmb", False),
]:
    assert is_nice_1(test[0]) == test[1]

def is_nice_2(str):
    has_pair_repeat = False
    has_split_repeat = False

    for i in range(len(str)-1):    
        for j in range(i+2, len(str)-1):
            if str[i:i+2] == str[j:j+2]:
                has_pair_repeat = True

        if i + 2 < len(str):
            if str[i] == str[i+2]:
                has_split_repeat = True

    return has_pair_repeat and has_split_repeat

for test in [
    ("qjhvhtzxzqqjkmpb", True),
    ("xxyxx", True),
    ("uurcxstgmygtbstg", False),
    ("ieodomkazucvgmuy", False),
]:
    assert is_nice_2(test[0]) == test[1]

def count_nice(input, validator):
    nice_count = 0

    for line in input:
        if validator(line):
            nice_count += 1

    return nice_count

print("Part 1: " + str(count_nice(input, is_nice_1)))
print("Part 2: " + str(count_nice(input, is_nice_2)))