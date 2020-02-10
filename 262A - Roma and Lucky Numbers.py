
x=0
n,k=map(int,input().split(" "))
X=input().split(" ")
for i in range(n):
    count=0
    for j in range(len(X[i])):
        if(X[i][j]=="4" or X[i][j]=="7"):
            count+=1


    if(count<=k):
        x=x+1
print(x)
