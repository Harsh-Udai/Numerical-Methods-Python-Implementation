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

y0=0
z0=0
x0=(1/l[0][0])*(l[0][-1] - l[0][1]*y0 - l[0][2]*z0)
y0=(1/l[1][1])*(l[1][-1] - l[1][0]*x0 - l[1][2]*z0)
z0=(1/l[2][2])*(l[2][-1] - l[2][0]*x0 - l[2][1]*y0)
print(x0,y0,z0)
x0=float("{0:.3f}".format(x0))
y0=float("{0:.3f}".format(y0))
z0=float("{0:.3f}".format(z0))

print("initial: ", x0, y0, z0)
i=1
a=x0
b=y0
c=z0

while(True):
    
    X=(1/l[0][0])*(l[0][-1] - l[0][1]*y0 - l[0][2]*z0)
    x0=X
    Y=(1/l[1][1])*(l[1][-1] - l[1][0]*x0 - l[1][2]*z0)
    y0=Y
    Z=(1/l[2][2])*(l[2][-1] - l[2][0]*x0 - l[2][1]*y0)
    z0=Z
    
    X=float("{0:.3f}".format(X))
    Y=float("{0:.3f}".format(Y))
    Z=float("{0:.3f}".format(Z))
    
    if(a==X and b==Y and c==Z):
        print("iteration",i,"Values: ",X,Y,Z, "<--Answer")
        break
    else:
        print("iteration",i,"Values: ",X,Y,Z)
    
    a=X
    b=Y
    c=Z
    i+=1
    