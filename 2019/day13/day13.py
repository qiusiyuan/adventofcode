import sys
import os
sys.path.append(os.path.join(os.getcwd() + '/..'))
from intcode import Program
import numpy as np

def format(input):
    return np.array(input).astype(np.int).reshape((-1,3))

def createMap(input):
    degree = np.max(input, axis=0)
    x = degree[0] + 1
    y = degree[1] + 1
    newTileMap = np.zeros((y, x))
    for i,j,tile in input:
        newTileMap[j][i] = tile
    return newTileMap

def countTile(tileMap):
    u, counter = np.unique(tileMap, return_counts=True)
    return counter

def moveLocation(tileMap):
    ball = np.where(tileMap == 4)
    paddle = np.where(tileMap == 3)
    ballp = (ball[1][0], ball[0][0])
    paddlep = (paddle[1][0], paddle[0][0])
    return int(ballp[0] > paddlep[0]) - int(ballp[0] < paddlep[0]) 

def update(tileMap, inputs):
    inputs = format(inputs)
    for line in inputs:
        x = line[0]
        y = line[1]
        if x == -1 and y == 0: #mark
            print("mark:", line[2])
        else:
            tileMap[y][x] = line[2]
    
def main():
    with open("input.txt", "r") as fd:
        machine_code = fd.read().split(',')
    machine_code[0] = '2'
    program = Program(machine_code)
    
    output, state = program.oneStep([])
    tileMap = createMap(format(output))
    print(countTile(tileMap))
    while state != -1:
        move = moveLocation(tileMap)
        output, state = program.oneStep([move])
        update(tileMap ,output)
    

if __name__ == "__main__":
    main()
