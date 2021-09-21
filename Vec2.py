import math


class Vector2:
    def __init__(self, X = 0, Y = 0):
        self.X = X
        self.Y = Y

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def setX(self, newX):
        self.X = newX
    
    def setY(self, newY):
        self.Y = newY
    
    def setVec(self, newX, newY):
        self.setX(newX)
        self.setY(newY)

    def vectorPrint(self):
        print("X = " + str(self.X) + ", Y = " + str(self.Y))

def DistanceBetweenVecs(VecA, VecB):
    val = math.sqrt( ((VecB.getX() - VecA.getX())**2) + ((VecB.getY() - VecA.getY())**2 ))
    return abs(val)