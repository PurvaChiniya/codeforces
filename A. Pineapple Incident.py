
t,s,x=map(int,input().split(" "))
n=x-t
if(n>1):
        
    if(n%s==0 or n%s==1):
      print("YES")
    else:
      print("NO")  
else:
    if(n==s or n==0):
      print("YES")
    else:  
      print("NO")
