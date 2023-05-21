import numpy as np
import FABFcn
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == "__main__":
    DoF = 4
    InitTheta = np.zeros((DoF+2,1)) # t1 will start at [1,0] element
    InitTheta[1,0] = 90 # t1 = 90
    LoF = 10 # Length of Freedom
    Joint = FABFcn.InitRobotNPoint(NumberOfPoint=DoF,LengthEachLink=LoF,ThetaInit=InitTheta)
    NewJoint,Angle = FABFcn.FABRIK(NumberOfPoint=DoF,Point=Joint,TargetPoint=[25,10,10])
    #print(FABFcn.Distance(NewJoint[0,:],NewJoint[1,:]))
    #print(NewJoint)
    FABFcn.Draw(Joint=NewJoint,xlim=[0,40],ylim=[0,40])
    print(FABFcn.JointAngle(NewJoint[1,:],NewJoint[2,:],NewJoint[3,:]))
    pass

