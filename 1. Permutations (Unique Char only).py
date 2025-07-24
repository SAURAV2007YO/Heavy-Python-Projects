#  i fixed it my way;
S = str(input("Enter a string with all unique charecters: "))


SS = 0
a = []
for SS in range(len(S)):
    a.append(S[SS])
SS = SS+1

print(a)

Perms = []

k=0
# l = []; complete inefficiency
m = [] # why did i put a m=[0] here, Biggest Mistake Number 2
#anyway both m and l were the same size even if i was inefficient haha
for k in range(len(S)-1):
    # l.append(len(S)-1-k)
    m.append(0)
k= k+1



z=0
c = m.copy()
b= a.copy()
perm = ""
# for i in range(len(S)-1):
while z>=0:
    i = z%(len(S)-1) # Brilliant Fix !!!

    perm = perm + b[c[i]]
    b.pop(c[i])

    if i == len(S)-2:
        
        perm = perm + b[0]
        Perms.append(perm)
        # print(Perms) # No use 

        perm = ""
        # i == -1; haha a nice mistake; Biggest Mistake Number 1
        b= a.copy()

        # if c == l: a nice inefficiency haha
        #     break
        
        j=1
        for j in range(1, len(S)):
            if c[-j] < j:
                c[-j] = c[-j] +1   # Dekho Bc ye cheez kaam karti hai yahan!!!, List bakchodi karne ki zaroorat nahi hai haha!          
                break
            else:
                c[-j] = 0
            j=j+1
        
        if c==m:
            break

        print(c) # Just because it somewhat shows off my logic here haha
    #i=i+1
    z=z+1


print("The final List of perms are: ")
print(Perms)
