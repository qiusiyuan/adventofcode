import sys
import os
sys.path.append(os.path.join(os.getcwd() + '/..'))
from intcode import Program

class Node:
    def __init__(self, position, program, deep):
        self.program = program
        self.position = position
        self.deep = deep 

def printmap(visited):
    left = min([pos[0] for pos in visited])
    right = max([pos[0] for pos in visited])
    bottom = min([pos[1] for pos in visited])
    top = max([pos[1] for pos in visited])
    maps = [' '*(right-left + 1)*4 for x in range(top - bottom + 1)]

    for point in visited:
        x, y = point
        insert = str(visited[point])
        insert = ' '* (3 - len(insert)) + insert + ' '
        maps[y - bottom] = maps[y-bottom][:(x-left)*4] + insert + maps[y-bottom][(x-left+1)*4:]
    for line in maps:
        print(line)
def BFS(program):
    directions = {(1,0): '4', (-1, 0): '3', (0, 1): '1', (0, -1): '2'}
    queue = []
    head = Node((0, 0), program, 0)
    queue.append(head)
    visited ={(0,0): 0}
    while len(queue) > 0:
        curr = queue.pop(0)
        point = curr.position
        for dire in directions:
            newpoint = (point[0] + dire[0], point[1] + dire[1])
            if newpoint not in visited:
                newNode = Node(newpoint, curr.program.clone(), curr.deep + 1)
                out, state = newNode.program.oneStep([directions[dire]])
                if state == -1:
                    return -1
                out = out[0]
                if out == '2':
                    visited[(newpoint)] = "her"
                    printmap(visited)
                    return newNode.deep
                elif out == '1':
                    visited[(newpoint)] = newNode.deep
                    queue.append(newNode)
                else:
                    visited[(newpoint)] = "#"
    return None
                
def main():
    with open("input.txt", "r") as fd:
        machine_code = fd.read().split(',')
    program = Program(machine_code)
    print(BFS(program))

if __name__ == "__main__":
    main()