with open("input.txt", "r") as fd:
    digits = fd.read()

wide = 25
tall = 6

print(len(digits)/(wide*tall))

def findMin(digits):
    min0 = float('inf')
    min1 = 0
    min2 = 0

    for i in range(0,len(digits), wide*tall):
        count0=0
        count1=0
        count2=0
        for j in range(wide*tall):
            char = digits[i+j]
            if char == '0':
                count0 += 1
            if char == '1':
                count1 += 1
            if char == '2':
                count2 += 1
        if count0 < min0:
            print(count0, count1, count2)
            min1 = count1
            min2 = count2
            min0 = count0
    return min1*min2
print(findMin(digits))

def compose(digits):
    comp = ['2' for p in range(wide*tall)]

    for i in range(0,len(digits), wide*tall):
        for j in range(wide*tall):
            char = digits[i+j]
            if comp[j] == '2':
                comp[j] = char
    return comp

comp = ''.join(compose(digits))
with open('output.txt', 'w+') as wd:
    for li in range(tall):
        wd.write(comp[li*wide: (li+1)*wide])
        wd.write("\n")
    
import matplotlib.pyplot as plt
comp = compose(digits)
import numpy as np
img = np.array(comp).reshape(tall, wide).astype(np.float)

imgplot = plt.imshow(img)
plt.savefig('out.png')
