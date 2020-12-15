import math
def fun(x):
    return ((math.e)**x) - (3*x) - (math.sin(x))


a=0 # Lower Bound
b=1 # Upper Bound
i=0
z=0
while(True):
    # Mid Value
    
    
    c= b - (((b-a)/(fun(b)-fun(a))) * fun(b))
    
    c=float("{0:.4f}".format(c))
    
    print(a,b,fun(a),fun(b))
    a=b
    b=c
    
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