class Program:
    def __init__(self, machine_code):
        mc = {}
        for i, code in enumerate(machine_code):
            mc[i] = code
        self.machine_code = mc
        self.relative_base = 0
        self.curr = 0

    def fillparam(self, code):
        if code[-1] == '1' or code[-1] == '2' or code[-1] == '7' or code[-1] == '8':
            return '0'*(5-len(code)) + code
        if code[-1] == '3' or code[-1] == '4' or code[-1] == '9':
            return '0'*(3-len(code)) + code
        if code[-1] == '5' or code[-1] == '6':
            return '0'*(4-len(code)) + code

    def oneStep(self, inputs):
        outputmy = []
        i = 0
        while self.machine_code[self.curr] != '99':
            op = self.fillparam(self.machine_code[self.curr])
            if op[-1] == '1' or op[-1] == '2' or op[-1] == '7' or op[-1] == '8':
                input1_param = op[2]
                input2_param = op[1]
                output_param = op[0]
                if input1_param == '1':
                    input1 = self.machine_code.get(self.curr + 1, '0')
                elif input1_param == '0':
                    input1 = self.machine_code.get(int(self.machine_code[self.curr + 1]), '0')
                elif input1_param == '2':
                    input1 = self.machine_code.get(int(self.machine_code[self.curr + 1]) + self.relative_base, '0')
                if input2_param == '1':
                    input2 = self.machine_code.get(self.curr + 2, '0')
                elif input2_param == '0':
                    input2 = self.machine_code.get(int(self.machine_code[self.curr + 2]),'0')
                elif input2_param == '2':
                    input2 = self.machine_code.get(int(self.machine_code[self.curr + 2]) + self.relative_base,'0')
                input1 = int(input1)
                input2 = int(input2)
                if output_param == '1':
                    print("error")
                if output_param == '2':
                    output_pos = int(self.machine_code.get(self.curr + 3, '0')) + self.relative_base
                elif output_param == '0':
                    output_pos = int(self.machine_code.get(self.curr + 3, '0'))
                # if output_pos >= len(self.machine_code):
                #     print("invalid")
                
                if op[-1] == '1': #add
                    self.machine_code[output_pos] = str(input1 + input2)
                elif op[-1] == '2': #mul
                    self.machine_code[output_pos] = str(input1 * input2)
                elif op[-1] == '7':
                    if input1 < input2:
                        self.machine_code[output_pos] = '1'
                    else:
                        self.machine_code[output_pos] = '0'
                else:
                    if input1 == input2:
                        self.machine_code[output_pos] = '1'
                    else:
                        self.machine_code[output_pos] = '0'
                self.curr += 4
            elif op[-1] =='3':
                if i >= len(inputs):
                    return outputmy, 0
                input_param = op[0]
                if input_param == '1':
                    print("input error")
                elif input_param == '0':
                    self.machine_code[int(self.machine_code[self.curr + 1])] = inputs[i]
                    i += 1
                elif input_param == '2':
                    self.machine_code[int(self.machine_code[self.curr + 1]) + self.relative_base] = inputs[i]
                    i += 1
                self.curr += 2
            elif op[-1] =='4':
                input_param = op[0]
                if input_param == '1':
                    outputmy.append(self.machine_code.get(self.curr+1, '0'))
                elif input_param == '0':
                    outputmy.append(self.machine_code.get(int(self.machine_code.get(self.curr + 1, '0')), '0'))
                elif input_param == '2':
                    outputmy.append(self.machine_code.get(int(self.machine_code.get(self.curr + 1, '0')) + self.relative_base, '0'))
                self.curr += 2
            elif op[-1] == '5' or op[-1] == '6':
                input1_param = op[1]
                input2_param = op[0]
                if input1_param == '1':
                    input1 = self.machine_code.get(self.curr + 1, '0')
                elif input1_param == '0':
                    input1 = self.machine_code.get(int(self.machine_code[self.curr + 1]), '0')
                elif input1_param == '2':
                    input1 = self.machine_code.get(int(self.machine_code[self.curr + 1]) + self.relative_base, '0')
                if input2_param == '1':
                    input2 = self.machine_code.get(self.curr + 2,'0')
                elif input2_param == '0':
                    input2 = self.machine_code.get(int(self.machine_code[self.curr + 2]), '0')
                elif input2_param == '2':
                    input2 = self.machine_code.get(int(self.machine_code[self.curr + 2])  + self.relative_base, '0')
                input1 = int(input1)
                input2 = int(input2)
                if op[-1] == '5':
                    if input1 != 0:
                        self.curr = input2
                    else:
                        self.curr += 3
                else:
                    if input1 == 0:
                        self.curr = input2
                    else:
                        self.curr += 3
            elif op[-1] == '9':
                input_param = op[0]
                if input_param == '1':
                    input1 = self.machine_code[self.curr + 1]
                elif input_param == '0':
                    input1 = self.machine_code.get(int(self.machine_code[self.curr + 1]), '0')
                elif input_param == '2':
                    input1 = self.machine_code.get(int(self.machine_code[self.curr + 1]) + self.relative_base, '0')
                self.relative_base += int(input1)
                self.curr += 2
            else:
                print("error op")
        return outputmy, -1

