#i fixed it my way again; the issue was just with deepcopy and changing [0,-1] to [0,"A"] and nothing else

import copy

def BlankLinePrinter(c: int): # c must be an integer (obviously)
   i=0
   for i in range(int(c)):
        print()

SIn = 0
while SIn>=0:
    S = str(input("Enter a string (any): "))
    if len(S)>1:
        break
    print("Please Enter a string with length greater than 1")
    SIn = SIn +1


Perms = []

# 3 Things are made here
s2=1
charofS  = [[S[0],1]] # how many duplicates of a char are present (1 list for 1 str and not editable)
uniquechars = [S[0]]
for s2 in range(1,len(S)):
    s3 =0
    for s3 in range(len(charofS)):
        if (charofS[s3])[0] == S[s2]:  # Duplicate
            (charofS[s3])[1] = (charofS[s3])[1] + 1
            break

        if s3 == len(charofS)-1:  # Unique
            charofS.append([S[s2],1])
            uniquechars.append(S[s2])
    s3=s3+1
s2=s2+1

s4 = 0
m = []
for s4 in range(len(S)-1):
    m.append([0, "A"]) ######## -1 changed to A
s4= s4+1





#######################################################################

z=0
c = copy.deepcopy(m)        # master list
d = copy.deepcopy(charofS)   # containing how many duplicates of a char are "now remaining"
b= copy.deepcopy(uniquechars)  # temporary intermediate chars list
perm = ""
while z>=0:
    i = z%(len(S)-1)

    perm = perm+ b[(c[i])[0]]

    # print(f"perm = {perm}") # Test

    ###################### 
    if (c[i])[1] == "A":
        (c[i])[1] = len(b)-1

    # if z<=len(S)-1:
    #     print(f"c = {c}") # Test


    ######### Next b
    k=0
    for k in range(len(d)):
        if b[(c[i])[0]] == (d[k])[0]:
                #########################################
                if (d[k])[1] > 1:
                    (d[k])[1] = (d[k])[1] - 1
                else:
                    b.pop((c[i])[0]) 
                ############################################   
                break            
        k=k+1

    # print(f"b= {b}") # Test

    
    ########################################
    if i == len(S)-2:
        
        perm = perm + b[0]
        print(perm) ######## Test
        Perms.append(perm)
        perm = ""

        b= copy.deepcopy(uniquechars)
        d= copy.deepcopy(charofS)


        j=1
        for j in range(1, len(S)):
            if (c[-j])[0] < (c[-j])[1]:
                (c[-j])[0] = (c[-j])[0] +1
                break
            else:
                c[-j] = [0, "A"]

            j=j+1


        print(c)
        # print() #Test

        if c==m:
            break         
    z=z+1


BlankLinePrinter(3)
print("The Final List of all Permutations is:")
print(Perms)

BlankLinePrinter(2)
print(f"The total number of Permutations for [{S}] is: {len(Perms)}")
BlankLinePrinter(2)
