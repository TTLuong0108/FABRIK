import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from FABmath import cosd, sind, acosd, asind, math

def Draw(Joint):
    ax = plt.axes(projection='3d')
    x_data=Joint[:,0]
    y_data=Joint[:,1]
    z_data=Joint[:,2]
    ax.plot(x_data,y_data,z_data,"x")
    plt.show()
    pass

def InitRobotNPoint(NumberOfPoint, LengthEachLink, ThetaInit):
    DoF = NumberOfPoint + 1 # Degree Of Freedom / add to 1 unit to delete [0,0] element
    l = LengthEachLink
    L = np.zeros((DoF+1,1))
    Px = np.zeros((DoF+2,1))
    Py = np.zeros((DoF+2,1))
    Pz = np.zeros((DoF+2,1))
    ThetaInit = ThetaInit
    ThetaSum = 0

    for i in range(1,DoF+1):
        L[i,0] = l
        if(i>1):
            ThetaSum = ThetaSum + ThetaInit[i-1,0]
            Px[i,0] = Px[i-1,0] + L[i-1,0]*cosd(ThetaSum)
            Py[i,0] = 0
            Pz[i,0] = Pz[i-1,0] + L[i-1,0]*sind(ThetaSum)
        else:
            Px[i,0] = 0
            Py[i,0] = 0
            Pz[i,0] = 0
    Px[DoF+1,0] = Px[DoF,0] + L[DoF,0]*cosd(ThetaSum + ThetaInit[DoF,0])
    Pz[DoF+1,0] = Pz[DoF,0] + L[DoF,0]*cosd(ThetaSum + ThetaInit[DoF,0])
    Py[DoF+1,0] = 0

    P_joint = np.zeros((DoF+1,3))
    for i in range(1,DoF+1):
        P_joint[i,0] = Px[i,0]
        P_joint[i,1] = Py[i,0]
        P_joint[i,2] = Pz[i,0]
    return P_joint

def Distance(PositionA,PositionB):
    xa = PositionA[0]
    ya = PositionA[1]
    za = PositionA[2]

    xb = PositionB[0]
    yb = PositionB[1]
    zb = PositionB[2]
    return math.sqrt((xb-xa)**2 + (yb-ya)**2 + (zb-za)**2)

def FabRik(NumberOfPoint,Point,TargetPoint):
    DoF = NumberOfPoint + 1
    P = Point
    t = TargetPoint
    d = np.zeros((DoF+2,1))
    d_sum = 0
    lamda = np.zeros((DoF+2,1))
    r = np.zeros((DoF+2,1))
    tol = 0.1

    for i in range(1,DoF): # 1 to DoF-1
        d[i,0] = Distance(P[i+1,:],P[i,:])
        d_sum = d_sum + d[i,0]
    dist = Distance(P[0,:],t)
    if(dist > d_sum):
        for i in range(1,DoF): # 1 -> DoF-1
            r[i,0] = Distance(t,P[i,:])
            lamda[i,0] = d[i,0]/r[i,0]
            P[i+1,:] = (1-lamda[i,0])*P[i,:] + lamda[i,0]*t
    pass
if __name__ == "__main__":
    d = Distance([0,0,0],[0,1,0])
    Draw()
    print(d)