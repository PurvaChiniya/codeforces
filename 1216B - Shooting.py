n=int(input())
X=[int(x) for x in input().split(" ")]
c=0
j=0
ans=[]
while(set(X)!={0}):
  temp=max(X)
  for i in range(len(X)):
    if(X[i]==temp):
      c=c+X[i]*j+1
      X[i]=0
      j=j+1
      ans.append(i+1)
      break


print(c)
print(" ".join(str(v) for v in ans))
