from FABmath import cosd, sind, acosd, asind, math
import numpy as np

def TransMatrix(a,anpha,d,theta):
    DH_matrix = [[cosd(theta),-sind(theta)*cosd(anpha),sind(theta)*sind(anpha) ,a*cosd(theta)],
                 [sind(theta),cosd(anpha)*cosd(theta) ,-cosd(theta)*sind(anpha),a*sind(theta)],
                 [0          ,sind(anpha)             ,cosd(anpha)             ,d           ],
                 [0          ,0                       ,0                       ,1          ]]
    return np.array(DH_matrix)
#///---- [Main program] ----- ///////
def run(t1,t2,t3,t4,t5,t6,L1,L2,L3,L4,text):
    T01=TransMatrix(L1,0,0,0)
    T12=TransMatrix(0 , 90,0,t1)     
    T23=TransMatrix(L2,-90,0,t2)       
    T34=TransMatrix(0 , 90,0,t3)       
    T45=TransMatrix(L3,-90,0,t4)         
    T56=TransMatrix(0 , 90,0,t5)      
    T67=TransMatrix(L4, -90,0,t6) 
    if text == "T01":
        ans = T01
    elif text == "T02":
        ans = T01 @ T12
    elif text == "T03":
        ans = T01 @ T12 @ T23
    elif text == "T04":
        ans = T01 @ T12 @ T23 @ T34
    elif text == "T05":
        ans = T01 @ T12 @ T23 @ T34 @ T45
    elif text == "T06":
        ans = T01 @ T12 @ T23 @ T34 @ T45 @ T56
    elif text == "T07":
        ans = T01 @ T12 @ T23 @ T34 @ T45 @ T56 @ T67
    Px = round(ans[0,3],4)
    Py = round(ans[1,3],4)
    Pz = round(ans[2,3],4)
    return np.array([Px,Py,Pz])