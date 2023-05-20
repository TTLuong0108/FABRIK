import numpy as np
import math

RoundNumber = 3
ArcRoundNumber = 2

def cosd(input):  
    return round(math.cos(input*math.pi/180),RoundNumber)

def sind(input):
    return round(math.sin(input*math.pi/180),RoundNumber)

def acosd(input):
    return round(math.acos(input)*180/math.pi,ArcRoundNumber)

def asind(input):
    return round(math.asin(input)*180/math.pi,ArcRoundNumber)

if __name__ == "__main__":
    a = cosd(30)
    Acra = acosd(a)
    print(a)
    print(Acra)
    pass