da,db=map(int,input().split(" "))
if(da==9 and db==1):
  print(str(9)+" "+str(10))

elif(db-da==1):
  x=str(da)+str(9)
  y=str(db)+str(0)
  print(str(x)+" "+str(y))

elif(db-da==0):
  x=str(da)+str(3)
  y=str(db)+str(4)
  print(str(x)+" "+str(y))
else:
  print(-1)    
