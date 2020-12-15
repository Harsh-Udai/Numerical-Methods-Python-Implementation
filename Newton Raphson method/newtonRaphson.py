import math

def fun(x):
    return (x*math.sin(x)) + math.cos(x)

def fun_dash(x):
    return x*math.cos(x)

a=2 # Lower Bound
b=3 # Upper Bound
i=0
z=0
while(True):
    # Mid Value
    

    c= a - (fun(a)/fun_dash(a))
    
    c=float("{0:.4f}".format(c))
    
    
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