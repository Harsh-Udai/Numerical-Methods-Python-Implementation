B=[[1,0,0,2.2],   
   [0,2,0,2.8],
   [0,0,-2.5,-3]]    

import numpy as np
n=len(B)
x=np.zeros(n)
u=['x','y','z']
for i in range(n):
    
    if(B[i][i]==0.0):
        print("Divide by zero")
        break
        
        
    for j in range(n):
        if(i!=j):
            ratio=float(B[j][i]/B[i][i])
            
        for k in range(n+1):
            B[j][k]=B[j][k]-ratio*(B[i][k])
        

for i in range(n):
    x[i]=B[i][n]/B[i][i]
    
for i,y in zip(x,u):
    print(y, ":", i)