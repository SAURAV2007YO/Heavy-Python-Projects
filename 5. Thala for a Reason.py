a = input("Enter desired Word/Number: ")

##### Functions to be Used in the Next Parts

def typeValue(c):
   try: #checking for if int
      b= int(c)+1
      return 1
   except: # Which means its str
      return 0
   
def Sumofdigs(c): # For int only
   i=0
   sum= 0
   for i in range(0, len(str(c))):
      sum = sum + int(str(c)[i])
   i=i+1   

   return sum

def SpaceRemover(c): # For both Strings and Numbers
   b= ""
   for i in range(len(str(c))):
      if (str(c)[i]== " "):
        continue
      b= b+(str(c)[i])

   return b


################### Print String with +

b= SpaceRemover(a)

i=0
for i in range(len(str(b))-1):
   print(str(b[i]), end="+")
i=i+1
print(str(b)[-1], "=")


################### Print the number it is equal to

if (typeValue(b)== 1):
   print(Sumofdigs(b))
   if (Sumofdigs(b)==7):
      print("Thala for a Reason")
   else:
      print("Not Thala vro")   
else:
   print(len(str(b)))   
   if (len(str(b))==7):
      print("Thala for a Reason")
   else:
      print("Not Thala Vro")

#################

z= input()
print(z)
