import numpy as np
import FABFcn
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == "__main__":
    DoF = 4
    InitTheta = np.zeros((DoF+2,1)) # t1 will start at [1,0] element
    InitTheta[2,0] = 90 # t2 = 90
    LoF = 10 # Length of Freedom
    Joint = FABFcn.InitRobotNPoint(NumberOfPoint=DoF,LengthEachLink=LoF,ThetaInit=InitTheta)
    FABFcn.Draw(Joint=Joint)
    NewJoint = FABFcn.FABRIK(NumberOfPoint=DoF,Point=Joint,TargetPoint=[5,1,0])
    print(Joint[:,1])
    pass

