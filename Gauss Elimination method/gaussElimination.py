import numpy as np

A=[[4,3,2,960],      # x-y+z=1
   [1,3,1,510],    # -3x+2y-3z=-6
   [2,1,3,610]]      # 2x-5y+4z=5
n=len(A)
x=np.zeros(n)
u=['x','y','z']

for i in range(0,len(A)):
    
    if(A[i][i]==0.0):
        print("Divide by zero")
        break
        
    for j in range(i+1,n):
        ratio=A[j][i]/A[i][i]
        
        for k in range(0,n+1):
            A[j][k]=A[j][k] - ratio*(A[i][k])
            
            
x[n-1]=(A[n-1][n]/A[n-1][n-1])
for i in range(n-1):
    w=(n-1-i-1)
    
    dd=A[w][w]
    let=0
    for j in range(w+1,n):
        let=let+(x[j]*A[w][j])
        
    x[w]=(A[w][n]-let)/dd
    
for i,y in zip(x,u):
    print(y, ":", i)