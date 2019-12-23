import math

class Rules:
    def __init__(self):
        self.recipes = {}
        self.discount = {}
        
    def addRecipe(self, input):
        pre, post = input.split("=>")
        outcount, out = post.strip().split(" ")
        newRecipe = Recipe(out, int(outcount))
        for content in pre.split(","):
            newRecipe.addContents(content)
        self.recipes[out] = newRecipe

    def countORE(self, target, need):
        count = 0
        recipe = self.recipes[target]
        self.discount.setdefault(target, 0)
        dis = min(self.discount.get(target, 0), need)
        need -= dis
        self.discount[target] -= dis
        mul = 0
        if need != 0:
            mul = math.ceil(need/recipe.count)
    
        self.discount[target] += mul*recipe.count - need
        for material in recipe.recipe:
            if material == 'ORE':
                count += mul*recipe.recipe['ORE']
            else:
                count += self.countORE(material, mul*recipe.recipe[material])
        return count

class Recipe:
    def __init__(self, material, count):
        self.material = material
        self.count = count
        self.recipe = {}
    
    def __str__(self):
        string = ""
        for mat in self.recipe:
            string += str(self.recipe[mat]) + " " +mat + ", "
        string += "=>" + str(self.count) + " " + self.material
        return string

    def addContents(self, input):
        outcount, out = input.strip().split(" ")
        self.recipe[out] = int(outcount)

def main():
    with open('input.txt') as fd:
        lines = fd.read().splitlines()
    
    rule = Rules()
    for line in lines:
        rule.addRecipe(line)
    #1
    print(rule.countORE("FUEL", 1))

    #2
    target = 1000000000000
    fro = 2595245
    to = 2595248
    for i in range(fro,to):
        oreC = rule.countORE("FUEL", i)
        print(i, oreC)
    

if __name__ == "__main__":
    main()