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
def backward_newton(t,po,findfor):
    t=t
    p=po
    h=t[1]-t[0]
    xn=t[-1]
    x=findfor
    yn=p[-1]
    l=[]
    k=0
    master=len(p)
    while(k<len(t)-1):
        for i in range(0,len(p)-1):
            p[i]=(p[i+1]-p[i])
        
        b=float("{0:.4f}".format(p[master-2])) 
        k+=1
        master-=1
        l.append(b)
#     print(l)
    p_master=(x-xn)/h
    re=1
    y=p_master
    
    o=[]
    for i in range(0,len(l)):
        p_master=(y+i)*(re)
        o.append(p_master)
        re=p_master
#     print(o)
    final=yn
    for i in range(0,len(o)):
        final=final+((l[i]*o[i])/fact(i+1))
    #     print(l[i],o[i],l[i]*o[i])
#         print(final,fact(i+1))
    return final

n=int(input("Enter the n (no of observation) "))
for i in range(n):
    l=list(map(str,input("enter the values in-range/space separated ").split()))      #1941 1951 1961 1971 1981
    value_=list(map(str,input("enter the values space separated ").split()))          #20 24 29 36 46
    finder=list(map(float,input("enter the values to find for.. and for range type space separated ").split())) #1976
    values=chan(value_)
    
    if '-' in l[0]:
        new_input=input_format(l)
        new_values=prefix_sum(values)
        if(len(finder)>1):
            g=(backward_newton(new_input,new_values,finder[1]))
            h=(backward_newton(new_input,new_values,finder[0]))
            print("The answer is: ",g-h)
        else:
            print("The answer is: ",backward_newton(new_input,new_values,finder[0]))
        
    else:
        new_input=chan(l)
        new_values=values
        print("The answer is: ",backward_newton(new_input,new_values,finder[0]))
    