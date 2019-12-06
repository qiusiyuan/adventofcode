fst = 193651
lst = 649729
# fst = 111111
# lst = 111122

def isPass(num):
    isDup = False
    isInc = True
    string = str(num)
    p = string[0]
    for i in range(1,6):
        curr = string[i]
        if curr == p:
            isDup = True
        if p > curr:
            isInc = False
        p = curr
    return (isDup and isInc)
    
#1
# c = 0
# for i in range(fst, lst+1):
#     if isPass(i):
#         c += 1
# print(c)

#2
def matchDup2(num):
    string = str(num)
    p = string[0]
    c = 1
    for i in range(1,6):
        curr = string[i]
        if curr == p:
            c += 1
        else:
            if c == 2:
                return True
            c = 1
        p = curr
    return c==2

c = 0
for i in range(fst, lst+1):
    if isPass(i) and matchDup2(i):
        c += 1
print(c)