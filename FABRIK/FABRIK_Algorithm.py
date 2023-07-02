import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from FABmath import cosd, sind, acosd, asind, math, JointAngle
import FABFcn
from enum import Enum
#** [INIT] **
class Progress(Enum):
    INIT = 0
    ApllyToXOYDemension = 1
    ApllyToXOZDemension = 2
    END = 3

class SubProgress(Enum):
    INIT = 0
    FORWARD = 1
    BACKWARD = 2
    RECALCULATE = 3
    END = 4

ProgressVariable = 0
SubProgressVariable = 0
time = 0
ProgressChart = list()
SubProgressChart = list()
TimeList = list()

#** [SUB FUNCTION] **
def updateProgressChart():
    global ProgressChart
    global SubProgressChart
    global time
    global TimeList
    global ProgressVariable
    global SubProgressVariable

    time = time + 1
    TimeList.append(time)
    ProgressChart.append(ProgressVariable)
    SubProgressChart.append(SubProgressVariable)
#*** [MAIN FUNCTION] **
def run(NumberOfPoint,Point,TargetPoint):
    global ProgressVariable
    global SubProgressVariable
    global ProgressChart
    global SubProgressChart
    global time
    global TimeList
    while(ProgressVariable <= Progress.END.value):
        match ProgressVariable:
            case Progress.INIT.value:
                updateProgressChart()
                DoF = NumberOfPoint + 1
                P = Point
                t = TargetPoint
                d = np.zeros((DoF+2,1))
                lamda = np.zeros((DoF+2,1))
                r = np.zeros((DoF+2,1))
                Angle = np.zeros((DoF,2))
                d_sum = 0
                tol = 0.05
                ProgressVariable = Progress.ApllyToXOYDemension.value
            case Progress.ApllyToXOYDemension.value:
                SubProgressVariable = SubProgress.INIT.value
                while(SubProgressVariable <= SubProgress.END.value):
                    updateProgressChart()
                    match SubProgressVariable:
                        case SubProgress.INIT.value:
                            updateProgressChart()
                            for i in range(1,DoF): # 1 to DoF-1
                                d[i,0] = FABFcn.Distance(P[i+1,:],P[i,:])
                                d_sum = d_sum + d[i,0]
                            dist = FABFcn.Distance(P[0,:],t)
                            if(dist > d_sum):
                                for i in range(1,DoF): # 1 -> DoF-1
                                    r[i,0] = FABFcn.Distance(t,P[i,:])
                                    lamda[i,0] = d[i,0]/r[i,0]
                                    P[i+1,:] = (1-lamda[i,0])*P[i,:] + lamda[i,0]*t
                                    SubProgressVariable = SubProgress.END.value
                            else:
                                difA = FABFcn.Distance(P[DoF,:],t)
                                SubProgressVariable = SubProgress.FORWARD.value
                        case SubProgress.FORWARD.value:
                            updateProgressChart()
                            P[DoF,:] = t
                            for i in range(DoF-1,0,-1): # DoF-1 -> 1
                                r[i,0] = FABFcn.Distance(P[i+1,:],P[i,:])
                                lamda[i,0] = d[i,0]/r[i,0]
                                P[i,:] = (1-lamda[i,0])*P[i+1,:] + lamda[i,0]*P[i,:]
                                P[i,0] = round(P[i,0],3)
                                P[i,1] = round(P[i,1],3)
                                P[i,2] = round(P[i,2],3)
                            SubProgressVariable = SubProgress.BACKWARD.value
                        case SubProgress.BACKWARD.value:
                            updateProgressChart()
                            P[1,:] = [0,0,0]
                            for i in range(1,DoF): # 1 -> DoF-1
                                r[i,0] = FABFcn.Distance(P[i+1,:],P[i,:])
                                lamda[i,0] = d[i,0]/r[i,0]
                                P[i+1,:] = (1-lamda[i,0])*P[i,:] + lamda[i,0]*P[i+1,:]  
                                P[i,0] = round(P[i,0],3)
                                P[i,1] = round(P[i,1],3)
                                P[i,2] = round(P[i,2],3)
                                if i <= DoF-2 and i>=1:
                                    Angle[i,0] = JointAngle(P[i,:],P[i+1,:],P[i+2,:],demension="OXZ")
                                    Angle[i,1] = JointAngle(P[i,:],P[i+1,:],P[i+2,:],demension="OXY")
                            SubProgressVariable = SubProgress.RECALCULATE.value
                        case SubProgress.RECALCULATE.value:
                            updateProgressChart()
                            difA = FABFcn.Distance(P[DoF,:],t)
                            difA = round(difA,2) 
                            if(difA > tol):
                                SubProgressVariable = SubProgress.FORWARD.value
                            else:
                                SubProgressVariable = SubProgress.END.value
                        case SubProgress.END.value:
                            updateProgressChart()
                            P[0,:] = P[1,:]
                            Angle[0,0] = JointAngle([-10,0,0],P[1,:],P[2,:],demension="OXZ")
                            Angle[0,1] = JointAngle([-10,0,0],P[1,:],P[2,:],demension="OXY")
                            ProgressVariable = Progress.ApllyToXOZDemension.value
                            break

            case Progress.ApllyToXOZDemension.value:
                ProgressVariable = Progress.END.value
                time = time + 1
                TimeList.append(time)
                ProgressChart.append(ProgressVariable)
                SubProgressChart.append(SubProgressVariable)
            case Progress.END.value:
                time = time + 1
                TimeList.append(time)
                ProgressChart.append(ProgressVariable)
                SubProgressChart.append(SubProgressVariable)
                return P,Angle

if __name__ == "__main__":
    DoF = 3
    InitTheta = np.zeros((DoF+2,1)) # t1 will start at [1,0] element
    InitTheta[1,0] = 90 # t1 = 90
    LoF = 10 # Length of Freedom
    TargetPoint = [15,10,10]
    Joint = FABFcn.InitRobotNPoint(NumberOfPoint=DoF,LengthEachLink=LoF,ThetaInit=InitTheta)
    NewJoint,_ = run(NumberOfPoint=DoF,Point=Joint,TargetPoint=TargetPoint)
    FABFcn.DrawChart(ProgressChart,SubProgressChart,TimeList)
    FABFcn.Draw(Joint=NewJoint,TargetPoint=TargetPoint,xlim=[-10,40],ylim=[-10,40],zlim=[0,30])
