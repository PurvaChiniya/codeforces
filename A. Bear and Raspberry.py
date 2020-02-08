n,c=map(int,input().split(" "))
X=[int(x) for x in input().split(" ")]
A=[]
for i in range(n-1):
  A.append(X[i]-X[i+1])
for j in range(n-1):
  if(A[j]==max(A)):
    break
if(max(A)>0):
  if(X[j]-X[j+1]-c>0):
    print(X[j]-X[j+1]-c)
  else:
    print(0)
else:
  print(0)
