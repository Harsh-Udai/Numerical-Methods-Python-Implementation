# 3, Variable X,Y,Z
def dominance(l,n):
    c=0
    for i in range(n):
        a=l[i][i]
        b=sum(l[i])-a-l[i][-1]
        if(a>=b):
            c+=1

    if(c==n):
        return True
    else:
        return False
    

n=int(input())
l=[]
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)
    
print("So the matrix is:")
print(l)
print()
print("Matrix is Dominace",dominance(l,len(l)))
print()
ini=[]
for i in range(0,n):
    a=l[i]
    ini.append(l[i][-1]/l[i][i])
    
x0,y0,z0=ini[0],ini[1],ini[2]
x0=float("{0:.3f}".format(x0))
y0=float("{0:.3f}".format(y0))
z0=float("{0:.3f}".format(z0))

print("initial: ", x0, y0, z0)
i=1
while(True):
    
    X=(1/l[0][0])*(l[0][-1] - l[0][1]*y0 - l[0][2]*z0)
    Y=(1/l[1][1])*(l[1][-1] - l[1][0]*x0 - l[1][2]*z0)
    Z=(1/l[2][2])*(l[2][-1] - l[2][0]*x0 - l[2][1]*y0)
    
    
    X=float("{0:.3f}".format(X))
    Y=float("{0:.3f}".format(Y))
    Z=float("{0:.3f}".format(Z))
    
    if(x0==X and y0==Y and z0==Z):
        print("iteration",i,"Values: ",X,Y,Z, "<--Answer")
        break
    else:
        print("iteration",i,"Values: ",X,Y,Z)
    
    x0=X
    y0=Y
    z0=Z
    i+=1