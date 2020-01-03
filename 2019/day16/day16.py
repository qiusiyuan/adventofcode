def newPattern(state, base):
    new = []
    for i in range(len(base)):
        new += state * [base[i]]
    return new

def calculate(pattern, inputs):
    count = 0
    for i in range(len(inputs)):
        count += inputs[i]*pattern[(i+1)%len(pattern)]
        # count = count%10
    if count < 0 and count%10 != 0:
        return 10 - count%10
    else:
        return count%10

def onePhase(inputs):
    result = []
    state = 1
    base = [0, 1, 0, -1]
    while state <= len(inputs):
        pattern = newPattern(state, base)
        result.append(calculate(pattern, inputs))
        state += 1
    return result


def main():
    with open("input.txt", "r") as fd:
        inputline = fd.read()
    inputline = "12345123451234512345"
    inputs = [int(i) for i in inputline]
    for _ in range(100):
        inputs = onePhase(inputs)
    print(inputs)
    
if __name__ == "__main__":
    main()