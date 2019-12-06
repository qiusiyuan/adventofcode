with open("input.txt", "r") as fd:
    sep = fd.read().splitlines()

fst = sep[0].split(",")
snd = sep[1].split(",")

def load(wire):
    allpoint = set()
    curr = (0, 0)
    for i in wire:
        direc, dist = analyze(i)
        for p in range(1, dist+1):
            new_curr = (curr[0]+direc[0], curr[1]+direc[1]) 
            allpoint.add(new_curr)
            curr = new_curr
    return allpoint
    
# direction (x, y)
def analyze(input):
    direction = input[0]
    dist = int(input[1:])
    if direction == "R":
        dire = (1, 0)
    if direction == "L":
        dire = (-1, 0)
    if direction == "U":
        dire = (0, 1)
    if direction == "D":
        dire = (0, -1)
    return dire, dist

def findMinimum(set1, set2):
    common = set1.intersection(set2)
    if len(common) == 0:
        print("No intersection")
        return
    miniset = None
    minimum = float("inf")
    for inter in common:
        dist = inter[0]+inter[1]
        if  dist < minimum:
            minimum = dist
            miniset = inter
    return minimum, miniset

def calculateSteps(common, wire):
    step_dict = {}
    for val in common:
        step_dict[val] = 0
    curr = (0, 0)
    steps = 0
    for i in wire:
        direc, dist = analyze(i)
        for p in range(1, dist+1):
            new_curr = (curr[0]+direc[0], curr[1]+direc[1]) 
            steps += 1
            if new_curr in step_dict and step_dict[new_curr] == 0:
                step_dict[new_curr] = steps
            curr = new_curr
    return step_dict

def minimumStep(dict1, dict2):
    minimum = float("inf")
    for key in dict1.keys():
        sums  = dict1[key] + dict2[key] 
        minimum = min(sums, minimum)
    return minimum


fset = load(fst)
sset = load(snd)

# 1
minimum, miniset = findMinimum(fset, sset)
print(minimum, miniset)

#2
common = fset.intersection(sset)
dict1 = calculateSteps(common, fst)
dict2 = calculateSteps(common, snd)
print(minimumStep(dict1, dict2))
