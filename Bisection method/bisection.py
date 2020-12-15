import math
def fun(x):
    return (x-math.cos(x))

# print(fun(1))

a=0 # Lower Bound
b=1 # Upper Bound
i=0
z=0
while(True):
    # Mid Value
    c=(a+b)/2
    
    c=float("{0:.4f}".format(c))
    op=float("{0:.4f}".format(fun(c)))
    print(a,b)
    print("Mid Value with function value",c,op)
    if(fun(a)*fun(c)<0):
        print("B is changed to c")
        b=c
        
    else:
        print("A is changed to c")
        a=c
    
    b=float("{0:.4f}".format(b))
    a=float("{0:.4f}".format(a))
    
    
    
    print("It is ",i," Iteration")
    print("..................................")
    i+=1
    if(z==c):
        print("Root Found, Yeah :)")
        print(c)
        break
    
    z=c