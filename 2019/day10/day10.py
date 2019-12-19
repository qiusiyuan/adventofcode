with open('input.txt', 'r') as fd:
    maps = fd.read().splitlines()

import math 
def can_detect(x,y, maps):
    dire = {}
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "#" and (i != y or j != x):
                if math.atan2(i - y,j-x) not in dire:
                    dire[math.atan2(i - y, j-x)] = [(j,i)]
                else:
                    dire[math.atan2(i - y, j-x)].append((j,i))
    return dire
max_dire = None
maxc = 0
maxx = 0
maxy = 0
for i in range(len(maps)):
    for j in range(len(maps[i])):
        if maps[i][j] == "#":
            dire = can_detect(j, i, maps)
            if len(dire) > maxc:
                maxc = len(dire)
                max_dire = dire
                maxx = j
                maxy = i
print(maxc, maxx, maxy)

def sortKey(key):
    newK = key
    if  - math.pi/2 > newK >= - math.pi :
        newK = newK + 2* math.pi
    return newK

keys = sorted(max_dire.keys(), key = sortKey)
print(keys)
def closest(key, x, y):
    if len(max_dire[key]) == 0:
        return None
    close = None
    min_distance = float('inf')
    for px, py in max_dire[key]:
        distance = (px-x)**2+(py-y)**2 
        if distance < min_distance:
            min_distance = distance
            close = (px, py)
    max_dire[key].remove(close)
    return close

curr = 0
close = None
for s in range(200):
    key = keys[curr]
    close = closest(key, maxx, maxy)
    curr = (curr + 1)%len(keys)
print(close)