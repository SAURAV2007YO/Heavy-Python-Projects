################### Taking N>=1 Value of N for which a NxN square is tobe generated

w1=0
while w1>=0:
    N= int(input("Enter Number to generate the n x n square: "))
    if(N>=1):
        break
    w1=w1+1


###################### making a NxN Zero matrix

#Making N Rows
i=0 
a= []
for i in range(N):
    a.append([])

#Making N Columns
i=0
for i in range(N):
    j=0
    for j in range(N):
        (a[i]).append(0)





################### Actual Code

f=0
for f in range(N):
    n= N-(2*f)
    NPS = int((N**2)-(n**2))
    P= int((N-n)/2)
    
    if n<=0:
        break
    if n==1:
        (a[int(N/2)])[int(N/2)] = int(N**2)
        break
    
    t=0
    for t in range(n-1):
        (a[P])[P+t] = int(NPS+(0*(n-1))+1+t)

    l=0
    for l in range(n-1):
        (a[P+l])[P+n-1] = int(NPS+(1*(n-1))+1+l)

    m=0
    for m in range(n-1):
        (a[P+n-1])[P+n-1-m] = int(NPS+(2*(n-1))+1+m)

    q=0
    for q in range(n-1):
        (a[P+n-1-q])[P] = int(NPS+(3*(n-1))+1+q)








#### Adding Blank Space infront of every element to make the whole matrix in a square shape 
x1=0
for x1 in range(N):
    x2=0
    for x2 in range(N):
        x3=0
        ccc= str((a[x1])[x2])
        for x3 in range(len(str((a[x1])[x2]))+1,len(str(N**2))+1):
            ccc = " " + ccc
        x3 = x3+1

        (a[x1])[x2] = ccc
    x2= x2+1
x1= x1+1

        
#Printing the Final Matrix
cc=0
for cc in range(N):
    print(a[cc])


# For making it into an exe file
z=input()
print(z)
