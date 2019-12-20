with open("input.txt", "r") as fd:
    machine_code = fd.read().split(',')

def fillparam(code):
    if code[-1] == '1' or code[-1] == '2' or code[-1] == '7' or code[-1] == '8':
        return '0'*(5-len(code)) + code
    if code[-1] == '3' or code[-1] == '4' or code[-1] == '9':
        return '0'*(3-len(code)) + code
    if code[-1] == '5' or code[-1] == '6':
        return '0'*(4-len(code)) + code

def process(machine_code, relative_base, curr, inputs):
    outputmy = []
    i = 0
    while machine_code[curr] != '99':
        op = fillparam(machine_code[curr])
        if op[-1] == '1' or op[-1] == '2' or op[-1] == '7' or op[-1] == '8':
            input1_param = op[2]
            input2_param = op[1]
            output_param = op[0]
            if input1_param == '1':
                input1 = machine_code.get(curr + 1, '0')
            elif input1_param == '0':
                input1 = machine_code.get(int(machine_code[curr + 1]), '0')
            elif input1_param == '2':
                input1 = machine_code.get(int(machine_code[curr + 1]) + relative_base, '0')
            if input2_param == '1':
                input2 = machine_code.get(curr + 2, '0')
            elif input2_param == '0':
                input2 = machine_code.get(int(machine_code[curr + 2]),'0')
            elif input2_param == '2':
                input2 = machine_code.get(int(machine_code[curr + 2]) + relative_base,'0')
            input1 = int(input1)
            input2 = int(input2)
            if output_param == '1':
                print("error")
            if output_param == '2':
                output_pos = int(machine_code.get(curr + 3, '0')) + relative_base
            elif output_param == '0':
                output_pos = int(machine_code.get(curr + 3, '0'))
            # if output_pos >= len(machine_code):
            #     print("invalid")
            
            if op[-1] == '1': #add
                machine_code[output_pos] = str(input1 + input2)
            elif op[-1] == '2': #mul
                machine_code[output_pos] = str(input1 * input2)
            elif op[-1] == '7':
                if input1 < input2:
                    machine_code[output_pos] = '1'
                else:
                    machine_code[output_pos] = '0'
            else:
                if input1 == input2:
                    machine_code[output_pos] = '1'
                else:
                    machine_code[output_pos] = '0'
            curr += 4
        elif op[-1] =='3':
            if i >= len(inputs):
                return outputmy, curr, relative_base
            input_param = op[0]
            if input_param == '1':
                print("input error")
            elif input_param == '0':
                machine_code[int(machine_code[curr + 1])] = inputs[i]
                i += 1
            elif input_param == '2':
                machine_code[int(machine_code[curr + 1]) + relative_base] = inputs[i]
                i += 1
            curr += 2
        elif op[-1] =='4':
            input_param = op[0]
            if input_param == '1':
                outputmy.append(machine_code.get(curr+1, '0'))
            elif input_param == '0':
                outputmy.append(machine_code.get(int(machine_code.get(curr + 1, '0')), '0'))
            elif input_param == '2':
                outputmy.append(machine_code.get(int(machine_code.get(curr + 1, '0')) + relative_base, '0'))
            curr += 2
        elif op[-1] == '5' or op[-1] == '6':
            input1_param = op[1]
            input2_param = op[0]
            if input1_param == '1':
                input1 = machine_code.get(curr + 1, '0')
            elif input1_param == '0':
                input1 = machine_code.get(int(machine_code[curr + 1]), '0')
            elif input1_param == '2':
                input1 = machine_code.get(int(machine_code[curr + 1]) + relative_base, '0')
            if input2_param == '1':
                input2 = machine_code.get(curr + 2,'0')
            elif input2_param == '0':
                input2 = machine_code.get(int(machine_code[curr + 2]), '0')
            elif input2_param == '2':
                input2 = machine_code.get(int(machine_code[curr + 2])  + relative_base, '0')
            input1 = int(input1)
            input2 = int(input2)
            if op[-1] == '5':
                if input1 != 0:
                    curr = input2
                else:
                    curr += 3
            else:
                if input1 == 0:
                    curr = input2
                else:
                    curr += 3
        elif op[-1] == '9':
            input_param = op[0]
            if input_param == '1':
                input1 = machine_code[curr + 1]
            elif input_param == '0':
                input1 = machine_code.get(int(machine_code[curr + 1]), '0')
            elif input_param == '2':
                input1 = machine_code.get(int(machine_code[curr + 1]) + relative_base, '0')
            relative_base += int(input1)
            curr += 2
        else:
            print("error op")
    return outputmy, -1, -1

# to dict
mc = {}
for i, code in enumerate(machine_code):
     mc[i] = code

def turn(currdirec, direc):
    # 0  turn left, 1 turn right
    x = 2*direc*currdirec[1] - currdirec[1]
    y = -2*direc*currdirec[0] + currdirec[0]
    return (x, y)

import numpy as np
import matplotlib.pyplot as plt
def painting(track, init):
    left = right = top = bottom = 0
    for point in track:
        left = min(left, point[0])
        right = max(right, point[0])
        bottom = min(bottom, point[1])
        top = max(top, point[1])
    rows = top - bottom + 1
    cols = right - left + 1
    maps = np.zeros((rows, cols))
    print(maps.shape)
    for x in range(rows):
        for y in range(cols):
            maps[rows-1-x][y] = int(track.get((left + y, bottom + x), init))
    imgplot = plt.imshow(maps)
    plt.savefig('out.png')

init = '0'
track = {}
currposition = (0, 0)
currdirec = (0, 1)
curr = 0
relative_base = 0
state = '0'
out, curr, relative_base = process(mc, relative_base, curr, [state])
while curr != -1:
    paint = out[0]
    direc = int(out[1])
    track[currposition] = paint
    currdirec = turn(currdirec, direc)
    currposition = (currposition[0] + currdirec[0], currposition[1] + currdirec[1])
    state = track.get(currposition, init)
    out, curr, relative_base = process(mc, relative_base, curr, [state])
    
print(len(track))


painting(track, init)




