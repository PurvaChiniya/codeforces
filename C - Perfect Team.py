q=int(input())
for _ in range(q):
  c,m,x=map(int,input().split(" "))

  team=0
  if(c>=x and m>=x):
    team=team+x
    #print('ff')
    #print(team) 
    c=c-x
    m=m-x
    x=0
    if(c>0 and m>0):
      a=max(c,m)
      b=min(c,m)
      
      if(b!=a and b>0 and a>0 ):
        if(2*b<=a):
          team=team+b
        else:
          n=(a-b)
          b=b-n
          a=a-(2*n)
          team=team+n
          #print("II")
          #print(a,b)
          #print(team)
      
      if(c>0 and m>0):
        if(a==b):
          if(a%3==0 or a%3==1):
            team=team+(2*(a//3))
            
          elif(a%3==2):
            team+=(2*(a//3))+1  
            #print("III")
            #print(team)
        
    print(team)
        
  else:
    team=team+min(c,m)
    print(team)
