with open("day-07.in") as file:
    input = file.readlines()

with open("day-07.testin") as file:
    test_input = file.readlines()

def build_circuit(instructions):
    circuit = {}

    for line in instructions:
        left, right = line.strip().split(" -> ")
        circuit[right] = left

    return circuit

def evaluate(circuit, value):
    if isinstance(value, int) or value.isnumeric():
        return int(value)

    expr = circuit[value]

    if isinstance(expr, int) or expr.isnumeric():
        circuit[value] = int(expr)
        return circuit[value]

    expr_split = expr.split()

    if len(expr_split) == 1: # int value
        circuit[value] = evaluate(circuit, expr_split[0])
    elif len(expr_split) == 2: # NOT
        circuit[value] = ~evaluate(circuit, expr_split[1]) % 65536
    else:
        match expr_split[1]:
            case "AND":
                circuit[value] = evaluate(circuit, expr_split[0]) & evaluate(circuit, expr_split[2])
            case "OR":
                circuit[value] = evaluate(circuit, expr_split[0]) | evaluate(circuit, expr_split[2])
            case "LSHIFT":
                circuit[value] = evaluate(circuit, expr_split[0]) << int(expr_split[2])
            case "RSHIFT":
                circuit[value] = evaluate(circuit, expr_split[0]) >> int(expr_split[2])
    
    return circuit[value]

for test in [
    ("d", 72),
    ("e", 507),
    ("f", 492),
    ("g", 114),
    ("h", 65412),
    ("i", 65079),
    ("x", 123),
    ("y", 456),
]:
    test_circuit = build_circuit(test_input)
    assert evaluate(test_circuit, test[0]) == test[1]

circuit = build_circuit(input)
signal_a = evaluate(circuit, "a")

print("Part 1: " + str(signal_a))

circuit = build_circuit(input)
circuit["b"] = signal_a

print("Part 1: " + str(evaluate(circuit, "a")))