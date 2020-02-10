n=int(input())
A=[int(x) for x in input().split(" ")]
B=[int(x) for x in input().split(" ")]
a=A[0]
b=B[0]
A=A[1:]
B=B[1:]
X=A.copy()
Y=B.copy()
count=0
c=0
while(len(A)>0 and len(B)>0):
    if(A[0]>B[0]):
        A.append(B[0])
        A.append(A[0])
        A.remove(A[0])
        B.remove(B[0])
        count=count+1
        #print(A)
        #print(B)
        #print(count)

    elif(A[0]<B[0]):
        B.append(A[0])
        B.append(B[0])
        B.remove(B[0])
        A.remove(A[0])
        count=count+1
        #print(A)
        #print(B)
        #print(count)
        
    if(A==X and B==Y):
        c=1
        #print(A)
        #print(B)
        #print(count)
        break
if(c==1):
    print("-1")
else:
    if(len(A)==0):
        print(str(count)+" "+str(2))              
    if(len(B)==0):
        print(str(count)+" "+str(1))              
    
