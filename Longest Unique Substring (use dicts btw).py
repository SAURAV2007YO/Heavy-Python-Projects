# dictionaries were made for such projects; i should have used them haha

a= str(input("Enter String to find the longest unique substring: "))


def ifCharinStr(x,y):
    j=0
    for j in range(len(y)):
        if x == y[j]:
            return j #Yes, char in str
    j=j+1

    return "NO"  #NO, char not in str


#printing input again
# print()
# print(a)
# print()



i=1
LS= a[0]
prevString = a[0]
for i in range(1,len(a)):
    duplpoint = ifCharinStr(a[i], prevString)
    # print(duplpoint) # Test 1

    if  duplpoint == "NO":                 
        prevString = prevString + a[i]
    else:
        prevString = a[i-len(prevString)+duplpoint+1:i+1]                            
    # print(f"for i={i} Current prevString = {prevString} ") # Test 2

    if len(prevString)>len(LS):
        LS = prevString
        # print(f"for i={i} Current LS = {LS} ") # Test 3
i=i+1


print(f"At the end of it all, The final LS = {LS}") 
