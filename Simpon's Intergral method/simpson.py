def func(x):
    return 1/(1+x)

def Simpson(a1,b1,n1):
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
    for i in range(1,len(y)-1):
        if(i%2==1):
            ans+=(4*(y[i]))
        else:
            ans+=(2*y[i])
    return ("Answer-> ",ans*(diff/3))

n=int(input("Enter the no. of inputs: "))
for _ in range(n):
    a1=int(input("Enter the lower range/lower limit: "))
    b1=int(input("Enter the upper range/upper limit: "))
    n1=int(input("Enter the value of n: "))
    print(Simpson(a1,b1,n1))