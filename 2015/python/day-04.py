import hashlib
import itertools

input = "bgvyzdsv"

def hash(key, num):
    bytes = str.encode(key + str(num))
    return hashlib.md5(bytes).hexdigest()

for test in [
    ("abcdef", 609043),
    ("pqrstuv", 1048970),
]:
    assert hash(test[0], test[1]).startswith("00000")

def first_hash_num(key, prefix):
    for i in itertools.count():
        if hash(key, i).startswith(prefix):
            return i

for test in [
    ("abcdef", "00000", 609043),
    ("pqrstuv", "00000", 1048970),
]:
    assert first_hash_num(test[0], test[1]) == test[2]


print("Part 1: " + str(first_hash_num(input, "00000")))
print("Part 2: " + str(first_hash_num(input, "000000")))