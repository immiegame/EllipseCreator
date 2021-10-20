from Vec2 import Vector2, DistanceBetweenVecs
import math

def GenerateEllipsePoints(center, objects, aDist, bDist, quartSize):
    EllipsePoints = []
    
    startingPoint = Vector2(center.getX() - aDist, center.getY())
    endingPoint = Vector2(center.getX() + aDist, center.getY())

    a = aDist * aDist
    b = bDist * bDist
    h = center.getX()
    k = center.getY()

    startDiff = endingPoint.getX() - startingPoint.getX()

    UpperSet = []
    LowerSet = []

    for i in range(0, 16):
        stepAmount = startingPoint.getX() + (i * startDiff / 16)
        y = math.sqrt(b * (1 - math.pow(stepAmount - h, 2) / a)) + k
        otherY = center.getY() - (y - center.getY())

        Up = Vector2(stepAmount, y)
        Down = Vector2(stepAmount, otherY)

        UpperSet.append(Up)
        LowerSet.append(Down)

    EllipsePoints.append(center)
    EllipsePoints.append(startingPoint)
    for i in range(0, len(UpperSet)):
        EllipsePoints.append(UpperSet[i])
    EllipsePoints.append(endingPoint)   
    for i in range(len(LowerSet), 0, -1):
        EllipsePoints.append(LowerSet[i])
    EllipsePoints.append(startingPoint)

    return EllipsePoints

def RotatePoints(points, objects):
    AnchorPoint = points[0]
    theta = GetRotateAngle(objects)
    for i in range(0, len(points)):
        newX = AnchorPoint.getX() + (points[i].getX() - AnchorPoint.getX()) * math.cos(theta) - (points[i].getY() - AnchorPoint.getY()) * math.sin(theta)
        newY = AnchorPoint.getY() + (points[i].getX() - AnchorPoint.getX()) * math.sin(theta) + (points[i].getY() - AnchorPoint.getY()) * math.cos(theta)
        points[i].setX(newX)
        points[i].setY(newY)


def GetMinDistance(Objects, Center, Pad, MinB):
    minDist = 0.0
    for i in range(0, len(Objects)):
        if(DistanceBetweenVecs(Center, Objects[i]) > minDist):
            minDist = DistanceBetweenVecs(Center, Objects[i])

    print("minDist = " + str(minDist))
    return minDist + Pad if minDist + Pad > MinB else MinB


def GetRotateAngle(Objects):
    average = Vector2()
    for i in range(0, len(Objects)):
        average.X += Objects[i].getX()
        average.Y += Objects[i].getY()
        if i == len(Objects) - 1:
            average.X /= len(Objects)
            average.Y /= len(Objects)
    
    rise = 0
    run = 0

    for i in range(0, len(Objects)):
        rise += (Objects[i].getX() - average.getX()) * (Objects[i].getY() - average.getY())
        run += (Objects[i].getX() - average.getX()) ** 2
    
    if run == 0:
        return math.pi / 2
    return math.atan(rise / run)


if __name__ == "__main__":

    EllipseCenter = Vector2(0, 0)
    ADistance = 0
    BDistance = 0
    Padding = 2

    EnclosedObjects = [
        Vector2(-1, 0),
        Vector2(1, 0),
        Vector2(2, -3),
    ]

    minBDist = 10
    ADistScale = 2 # A distance is always double B distance

    BDist = GetMinDistance(EnclosedObjects, EllipseCenter, Padding, minBDist)
    ADist = BDist * ADistScale

    points = GenerateEllipsePoints(EllipseCenter, EnclosedObjects, ADist, BDist, 4)
    RotatePoints(points, EnclosedObjects)