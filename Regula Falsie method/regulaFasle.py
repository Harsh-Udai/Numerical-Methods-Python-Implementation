import math

def fun(x):
    return 3*x + math.sin(x) - ((math.e)**x)

a=0 # Lower Bound
b=1 # Upper Bound
i=0
z=0
while(True):
    # Mid Value
    
    e1=fun(a)
    e2=fun(b)-fun(a)
    e3=b-a
    
    c=a-((e1/e2)*e3)
    
    c=float("{0:.4f}".format(c))
    
    
    if(fun(a)*fun(c)<0):
        print("B is changed to c")
        b=c
        
    else:
        print("A is changed to c")
        a=c
    
    b=float("{0:.4f}".format(b))
    a=float("{0:.4f}".format(a))
    
    
    print("Mid Value with function value",c,fun(c))
    print("It is ",i," Iteration")
    print("..................................")
    i+=1
    if(z==c):
        print("Root Found, Yeah :)")
        print(c)
        break
    
    z=c