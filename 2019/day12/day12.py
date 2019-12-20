


class System:
    def __init__(self):
        self.moons = []
        self.step = 0
    
    def addMoon(self, moon):
        self.moons.append(moon)
    
    def calculateVelocity(self):
        for i in range(len(self.moons)):
            moon = self.moons[i]
            for j in range(len(self.moons)):
                if j!= i:
                    otherMoon = self.moons[j]
                    moon.vx += self.gravity(otherMoon.x - moon.x)
                    moon.vy += self.gravity(otherMoon.y - moon.y)
                    moon.vz += self.gravity(otherMoon.z - moon.z)
    
    def gravity(self, dist):
        if dist > 0 :
            return 1
        elif dist < 0:
            return -1
        else:
            return 0

    def newPosition(self):
        for moon in self.moons:
            moon.x += moon.vx
            moon.y += moon.vy
            moon.z += moon.vz
    
    def oneStep(self):
        self.calculateVelocity()
        self.newPosition()
        self.step += 1

    def calculateEnergy(self):
        potential = lambda moon: abs(moon.x) + abs(moon.y) + abs(moon.z)
        kinetic = lambda moon: abs(moon.vx) + abs(moon.vy) + abs(moon.vz)

        total = 0
        for moon in self.moons:
            total += potential(moon)*kinetic(moon)
        return total

    def printSummary(self):
        print("After Step", self.step, "total Energy:", self.calculateEnergy())
        for moon in self.moons:
            print(moon)

    def copy(self):
        system = System()
        for moon in self.moons:
            new = Moon(moon.x, moon.y, moon.z)
            new.vx = moon.vx
            new.vy = moon.vy
            new.vz = moon.vz
            system.addMoon(new)
        return system

    def isEqual(self, other, axis = None):
        equal = True
        for i in range(len(self.moons)):
            thisMoon = self.moons[i]
            otherMoon = other.moons[i]
            if not thisMoon.isEqual(otherMoon, axis):
                equal = False
        return equal



class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def __str__(self):
        return("pos=<x= {x}, y= {y}, z={z}>, vel=<x= {vx}, y= {vy}, z={vz}>".format(x=self.x, y=self.y, z= self.z, vx = self.vx, vy = self.vy, vz = self.vz))

    def isEqual(self, other, axis = None):
        if axis == "x":
            return self.x == other.x and self.vx == other.vx
        if axis == 'y':
            return self.y == other.y and self.vy == other.vy
        if axis == 'z':
            return self.z == other.z and self.vz == other.vz
        return self.x == other.x and self.y == other.y and self.z == other.z and self.vx == other.vx and self.vy == other.vy and self.vz == other.vz
import math
def lcm(a, b, c):
    gcd1 = math.gcd(a, b)
    lcm1 = a*b//gcd1
    gcd2 = math.gcd(lcm1, c)
    return lcm1*c//(gcd2)

import time
def main1():
    
    system = System()
    system.addMoon(Moon(-13, 14, -7))
    system.addMoon(Moon(-18, 9, 0))
    system.addMoon(Moon(0, -3, -3))
    system.addMoon(Moon(-15, 3, -13))
    # system.addMoon(Moon(-1, 0, 2))
    # system.addMoon(Moon(2, -10, -7))
    # system.addMoon(Moon(4, -8, 8))
    # system.addMoon(Moon(3, 5, -1))
    
    previous = system.copy()
    xequal = False
    yequal = False
    zequal = False
    xc = yc = zc = None
    while not (xequal and yequal and zequal):
        system.oneStep()
        if system.isEqual(previous, axis = 'x'):
            xequal = True
        if system.isEqual(previous, axis = 'y'):
            yequal = True
        if system.isEqual(previous, axis = 'z'):
            zequal = True
        if xequal and xc == None:
            xc = system.step
        if yequal and yc == None:
            yc = system.step
        if zequal and zc == None:
            zc = system.step
    print(xc, yc, zc)
    print(lcm(xc, yc, zc))
    system.printSummary()
    
if __name__ == "__main__":
    start = time.time()
    main1()
    print(time.time() - start)