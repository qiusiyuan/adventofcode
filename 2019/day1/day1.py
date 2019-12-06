with open("input.txt", 'r') as fd:
    inputs = fd.read().splitlines()

fuel = lambda x: x//3 - 2
inputs = [int(i) for i in inputs]
fuels = [fuel(x) for x in inputs]
print(sum(fuels))

def fuel2(x):
    fuel = x//3 - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + fuel2(fuel)
fuels2 = [fuel2(x) for x in inputs]
print(sum(fuels2))