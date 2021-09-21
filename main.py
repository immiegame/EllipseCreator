from Vec2 import Vector2, DistanceBetweenVecs
import math

def GenerateEllipsePoints(center, objects, aDist, bDist, quartSize):
    EllipsePoints = []
    angleToA = math.atan(GetAverageSlope(objects))
    otherAngle = (90 * math.pi / 180) - angleToA


    angleToB = 0 
    if(GetAverageSlope(objects) == 0):
        angleToB = (90 * math.pi / 180)
    else:
        angleToB = math.atan( -1 / GetAverageSlope(objects))
    otherBAngle = (90 * math.pi / 180) - angleToB

    XDistToA = otherAngle * aDist
    YDistToA = angleToA * aDist
    XDistToB = otherBAngle * bDist
    YDistToB = angleToB * bDist

    APoint = Vector2(center.getX() + XDistToA, center.getY() + YDistToA)
    BPoint = Vector2(center.getX() + XDistToB, center.getY() + YDistToB)
    OppositeAPoint = Vector2(center.getX() - XDistToA, center.getY() - YDistToA)
    OppositeBPoint = Vector2(center.getX() - XDistToB, center.getY() - YDistToB)



    APoint.vectorPrint()
    OppositeAPoint.vectorPrint()
    BPoint.vectorPrint()
    OppositeBPoint.vectorPrint()

    EllipsePoints.append(APoint)

    return EllipsePoints


def GetMinDistance(Objects, Center, Pad, MinB):
    minDist = 0.0
    for i in range(0, len(Objects)):
        if(DistanceBetweenVecs(Center, Objects[i]) > minDist):
            minDist = DistanceBetweenVecs(Center, Objects[i])

    print("minDist = " + str(minDist))
    return minDist + Pad if minDist + Pad > MinB else MinB


def GetAverageSlope(Objects):
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
    return rise / run


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

    GenerateEllipsePoints(EllipseCenter, EnclosedObjects, ADist, BDist, 4)