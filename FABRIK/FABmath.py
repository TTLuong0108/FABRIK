import numpy as np
import math

RoundNumber = 4
ArcRoundNumber = 2

def cosd(input):  
    input = round(input,RoundNumber)
    return round(math.cos(input*math.pi/180),RoundNumber)

def sind(input):
    input = round(input,RoundNumber)
    return round(math.sin(input*math.pi/180),RoundNumber)

def acosd(input):
    input = round(input,ArcRoundNumber)
    return round(math.acos(input)*180/math.pi,ArcRoundNumber)

def asind(input):
    input = round(input,ArcRoundNumber)
    return round(math.asin(input)*180/math.pi,ArcRoundNumber)

def JointAngle(A,B,C,demension):
    if demension == "OXYZ":
        xA = A[0] 
        yA = A[1]
        zA = A[2]
        xB = B[0]
        yB = B[1]
        zB = B[2]
        xC = C[0]
        yC = C[1]
        zC = C[2]
    elif demension == "OXY":
        xA = A[0] 
        yA = A[1]
        zA = 0
        xB = B[0]
        yB = B[1]
        zB = 0
        xC = C[0]
        yC = C[1]
        zC = 0
    elif demension == "OXZ":
        xA = A[0] 
        yA = 0
        zA = A[2]
        xB = B[0]
        yB = 0
        zB = B[2]
        xC = C[0]
        yC = 0
        zC = C[2]

    angle_BAC = 0
    angle_BCA = 0
    Vector_AB = B-A
    Vector_BC = C-B

    AB = math.sqrt( (xA-xB)**2 + (yA-yB)**2 + (zA-zB)**2 )
    BC = math.sqrt( (xB-xC)**2 + (yB-yC)**2 + (zB-zC)**2 )
    AC = math.sqrt( (xA-xC)**2 + (yA-yC)**2 + (zA-zC)**2 )
    angle_BAC = acosd((AB**2+AC**2-BC**2)/(2*AB*AC))
    angle_BCA = acosd((BC**2+AC**2-AB**2)/(2*BC*AC))

    Z = -(Vector_AB[2]/AB)*(Vector_BC[0]/BC) + (Vector_AB[0]/AB)*(Vector_BC[2]/BC)
    Z = np.sign(Z)
    return Z*(angle_BAC + angle_BCA)

if __name__ == "__main__":
    A = [0,0,0]
    B = [1,0,0]
    C = [1,0,1]
    #print(B[0])
    print(JointAngle(A,B,C))
    pass