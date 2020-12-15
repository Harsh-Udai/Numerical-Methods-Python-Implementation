def input_format(l):
    l1=[]
    for x in range(0,len(l)):
        val=0
        for i,j in enumerate(l[x]):
            if(j=='-'):
                val=l[x][i+1:]
                break
        l1.append(int(val))
    return l1

def prefix_sum(l):
    for i in range(1,len(l)):
        l[i]=l[i-1]+l[i]
    return l
def chan(l):
    l1=[]
    for i in l:
        l1.append(float(i))
    return l1

def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)

def forward_newton(t,po,findfor):
    p=[]
    for i in po:
        p.append(i)
    h=t[1]-t[0]
    xn=t[0]
    x=findfor
    yn=p[0]
    l=[]
    k=0
    # forward
    while(k<len(t)-1):
        for i in range(0,len(p)-1):
            p[i]=(p[i+1]-p[i])
        b=float("{0:.4f}".format(p[0]))   
        l.append(b)
        k+=1
    p=(x-xn)/h
    re=1
    y=p
    o=[]
    for i in range(0,len(l)):
        p=(y-i)*(re)
        o.append(p)
        re=p
    final=yn
    for i in range(0,len(o)):
        final=final+((l[i]*o[i])/fact(i+1))
    #     print(l[i],o[i],l[i]*o[i])
    return (final)

n=int(input("Enter the n (no of observation) "))
for i in range(n):
    l=list(map(str,input("enter the values in-range/space separated ").split()))      #0-40 40-60 60-80 80-100 100-120
    value_=list(map(str,input("enter the values space separated ").split()))          #250 120 100 70 50
    finder=list(map(float,input("enter the values to find for.. and for range type space separated ").split()))# 60 70 (Range)
    values=chan(value_)
    
    if '-' in l[0]:
        new_input=input_format(l)
        new_values=prefix_sum(values)
        if(len(finder)>1):
            g=(forward_newton(new_input,new_values,finder[1]))
            h=(forward_newton(new_input,new_values,finder[0]))
            print("The answer is: ",g-h)
        else:
            print("The answer is: ",forward_newton(new_input,new_values,finder[0]))
        
    else:
        new_input=chan(l)
        new_values=values
        print("The answer is: ",forward_newton(new_input,new_values,finder[0]))
    