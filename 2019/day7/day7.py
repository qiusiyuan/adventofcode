with open("input.txt", "r") as fd:
    machine_code = fd.read().split(',')

def fillparam(code):
    if code[-1] == '1' or code[-1] == '2' or code[-1] == '7' or code[-1] == '8':
        return '0'*(5-len(code)) + code
    if code[-1] == '3' or code[-1] == '4':
        return '0'*(3-len(code)) + code
    if code[-1] == '5' or code[-1] == '6':
        return '0'*(4-len(code)) + code

def process(machine_code, curr, inputs):
    outputmy = 0
    i = 0
    while curr< len(machine_code) and machine_code[curr] != '99':
        op = fillparam(machine_code[curr])
        if op[-1] == '1' or op[-1] == '2' or op[-1] == '7' or op[-1] == '8':
            input1_param = op[2]
            input2_param = op[1]
            output_param = op[0]
            if input1_param == '1':
                input1 = machine_code[curr + 1]
            else:
                input1 = machine_code[int(machine_code[curr + 1])]
            if input2_param == '1':
                input2 = machine_code[curr + 2]
            else:
                input2 = machine_code[int(machine_code[curr + 2])]
            input1 = int(input1)
            input2 = int(input2)
            if output_param == '1':
                print("error")
            output_pos = int(machine_code[curr + 3])
            if output_pos >= len(machine_code):
                print("invalid")
            else:
                if op[-1] == '1': #add
                    machine_code[output_pos] = str(input1 + input2)
                elif op[-1] == '2': #mul
                    machine_code[output_pos] = str(input1 * input2)
                elif op[-1] == '7':
                    if input1 < input2:
                        machine_code[output_pos] = 1
                    else:
                        machine_code[output_pos] = 0
                else:
                    if input1 == input2:
                        machine_code[output_pos] = 1
                    else:
                        machine_code[output_pos] = 0
            curr += 4
        elif op[-1] =='3':
            if i >= len(inputs):
                return outputmy, curr
            input_param = op[0]
            if input_param == '1':
                print("input error")
            else:
                machine_code[int(machine_code[curr + 1])] = inputs[i]
                i += 1
            curr += 2
        elif op[-1] =='4':
            input_param = op[0]
            if input_param == '1':
                print("output", machine_code[curr+1])
                outputmy = machine_code[curr+1]
            else:
                print("output", machine_code[int(machine_code[curr + 1])])
                outputmy = machine_code[int(machine_code[curr + 1])]
            curr += 2
        elif op[-1] == '5' or op[-1] == '6':
            input1_param = op[1]
            input2_param = op[0]
            if input1_param == '1':
                input1 = machine_code[curr + 1]
            else:
                input1 = machine_code[int(machine_code[curr + 1])]
            if input2_param == '1':
                input2 = machine_code[curr + 2]
            else:
                input2 = machine_code[int(machine_code[curr + 2])]
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
        else:
            print("error op")
    return outputmy, -1

from itertools import permutations 
  
# Get all permutations of [1, 2, 3] 
perm = permutations([5,6,7,8,9]) 

ans = []
for p in list(perm):
    machines = [machine_code.copy() for i in range(5)]
    currs = [0 for i in range(5)]
    fin = '0'
    print(p)
    # first loop
    for index in range(5):
        phase = p[index]
        curr = currs[index]
        nmachine = machines[index]
        nout, curr = process(nmachine, curr, [str(phase),fin])
        currs[index] = curr
        fin = nout
    while currs[-1] != -1:
        for index in range(5):
            curr = currs[index]
            nmachine = machines[index]
            nout, curr = process(nmachine, curr, [fin])
            currs[index] = curr
            fin = nout
    ans.append(int(fin))

print(max(ans))
print(ans)

