def func(x):
    return 1/(1+x)

def trapizoidal(a1,b1,n1):
    a=a1
    b=b1
    n=n1
    diff=(b-a)/n
    x=[]
    k=0
    for i in range(0,b):
        if(k==b):
            break
        x.append(k)
        x.append(k+diff)
        k=k+2*diff
    x.append(b)
    y=[]
    for i in x:
        y.append(func(i))
    ans=func(a)+func(b)
    ans+= 2*sum((y[1:-1]))
    ans= (ans*(diff/2))
    return("Answer -> ",ans)

n=int(input("Enter the no. of inputs: "))
for _ in range(n):
    a1=int(input("Enter the lower range/lower limit: "))
    b1=int(input("Enter the upper range/upper limit: "))
    n1=int(input("Enter the value of n: "))
    print(trapizoidal(a1,b1,n1))