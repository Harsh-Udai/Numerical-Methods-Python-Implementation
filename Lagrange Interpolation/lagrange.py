def lagrange(x,y,find):
    ans=0
    for i in range(0,len(x)):
        mult=y[i]
        main1=1
        main2=1
        for j in range(0,len(x)):
            if(i!=j):
                main1*=(find-x[j])
                main2*=(x[i]-x[j])
        ans+=(mult*(main1/main2))
    return(ans)   
    
x=[0,1,4,5,6,7,8]
y=[170,168,172,169,168,165,167]
find=9
lagrange(x,y,find)