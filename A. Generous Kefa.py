n,k=map(int,input().split(" "))
s=input()
l=list(set(s))
count=[]
for i in range(len(l)):
  count.append(s.count(l[i]))
  if(count[i]>k):
    print("NO")
    c=0
    break
  else:
    c=1  

if(c>0):
  print("YES")
