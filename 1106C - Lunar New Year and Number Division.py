n=int(input())
X=[int(x) for x in input().split(" ")]
X.sort()
c=0
for i in range(int(n/2)):
  c=c+((X[i]+X[n-1-i])**2)

print(c)  
