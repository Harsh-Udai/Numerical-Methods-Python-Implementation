def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)
def Stirling(t1,p1,fi):
    t=t1                 #[20,25,30,35,40]
    p=p1                 #[49225,48316,47236,45926,44306]
    mid=len(t)//2
    h=t[1]-t[0]
    xn=t[mid]
    x=fi[0]
    yn=p[mid]
    l=[]
    k=0
    p1=(x-xn)/h
    master=mid
    while(k<len(t)-1):
        for i in range(0,len(p)-1):
            p[i]=(p[i+1]-p[i])
        if(k%2==0):
            b=float("{0:.4f}".format(p[master])) 
            b1=float("{0:.4f}".format(p[master-1])) 
            master-=1
        else:
            b=float("{0:.4f}".format(p[master]))
            b1=0
        k+=1
        l.append([b,b1])
    o=[p1,p1**2]
    count=0
    hh=1
    for i in range(0,len(t)-3):
        if(i%2==0):
            d=o[1]-(hh)**2
            d=d*o[-2]
            d=float("{0:.4f}".format(d)) 
            o.append(d)
        else:
            d=o[-1]
            d=d*p1
            d=float("{0:.4f}".format(d)) 
            o.append(d)
        count+=1
        if(count==2):
            count=0
            hh+=1
    final=yn
    for i in range(0,len(o)):
        if(l[i][1]==0):
            final+=((((l[i][0]+l[i][1]))*o[i])/fact(i+1))
        else:
            final+=((((l[i][0]+l[i][1])/2)*o[i])/fact(i+1))
    return(final)

n=int(input("Enter the n (no of observation) "))
for i in range(n):
    l=list(map(float,input("enter the values space separated ").split()))      
    value_=list(map(float,input("enter the values space separated ").split()))          
    finder=list(map(float,input("enter the values to find for..").split()))
    print(Stirling(l,value_,finder))