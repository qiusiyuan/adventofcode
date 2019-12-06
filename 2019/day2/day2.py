with open("input.txt", "r") as fd:
    machine_code = fd.read().split(',')
machine_code = [int(i) for i in machine_code]
machine_code[1] = 12
machine_code[2] = 2
def process(machine_code):
    curr = 0
    while curr< len(machine_code)-3 and machine_code[curr] != 99:
        op = machine_code[curr]
        input1 = machine_code[machine_code[curr + 1]]
        input2 = machine_code[machine_code[curr + 2]]
        output_pos = machine_code[curr + 3]
        if op == 1:#add
            if output_pos < len(machine_code):
                machine_code[output_pos] = input1 + input2
            else:
                print("invalid")
        if op == 2:#mul
            if output_pos < len(machine_code):
                machine_code[output_pos] = input1 * input2
            else:
                print("invalid")
        curr += 4
    return machine_code[0]

for i in range(100):
    for j in range(100):
        machine_code[1] = i
        machine_code[2] = j
        if process(machine_code.copy()) == 19690720:
            print(i,j)

