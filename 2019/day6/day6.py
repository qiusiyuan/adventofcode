with open("input.txt", "r") as fd:
    inputlines = fd.read().splitlines()

def splitr(route):
    jj = route.split(")")
    main = jj[0]
    ob = jj[1]
    return main, ob

all_dict = {}

for route in inputlines:
    main, ob = splitr(route)
    if ob not in all_dict:
        all_dict[ob] = main

dp = {} 
def count(ob):
    if ob in dp:
        return dp[ob]
    main = all_dict[ob]
    if main not in all_dict:
        return 1
    if main in dp:
        return dp[main] + 1
    counts = count(main) + 1
    dp[ob] = counts
    return counts
c = 0
for ob in all_dict:
    c += count(ob)
print(c)
    
#2 
def count_route(obj):
    orbting = {}
    main  = all_dict[obj]
    s = 0
    while main in all_dict:
        orbting[main] = s
        main = all_dict[main]
        s += 1
    orbting[main] = s
    return orbting
def minimum_route(o1, o2):
    minimum = float('inf')
    for key in o1.keys():
        if key in o2:
            minimum = min(o1[key] + o2[key], minimum)
    return minimum

o1 = count_route("YOU")
o2 = count_route("SAN")
print(minimum_route(o1,o2))
