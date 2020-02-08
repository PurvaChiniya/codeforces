d,sumTime=map(int,input().split(" "))
Min=[]
Max=[]
for _ in range(d):
    min_,max_=map(int,input().split(" "))
    Min.append(min_)
    Max.append(max_)
min_sum=sum(Min)
max_sum=sum(Max)
if (min_sum<=sumTime<=max_sum):
    print("YES")
    for i in range(d):
        if(sumTime==sum(Min)):
            break
        else:
            if (Max[i]-Min[i]>=(sumTime-sum(Min))):
                Min[i]=Min[i]+(sumTime-sum(Min))
            if (0<Max[i]-Min[i]<(sumTime-sum(Min))):
                Min[i]=Min[i]+Max[i]-Min[i]
                  
    print(" ".join(str(v) for v in Min))              
else:
    print("NO") 
