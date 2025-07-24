# a way by which you can do it in O(log(n)) steps only!

i=0
a=[]
while i>=0:
    b= input(f"Enter {len(a)+1}th Number('Break' to Stop): ")
    if b=="Break":
        break
    
    try:
        c= int(b)+1         
    except:
        print("Please enter a number only")
        continue
    
    a.append(b) 
i=i+1

print(a)

b=[]
b.insert(0,a[0])

i=1
for i in range(1,len(a)):
    if float(a[i])<float(b[0]):
        b.insert(0,a[i])
    elif float(a[i])>float(b[-1]):
        b.insert(len(b),a[i])       
    else:
        j=0
        for j in range(len(b)-1):
            if float(b[j])<=float(a[i])<float(b[j+1]):      # Fix this for the equal cases!!!!
                b.insert(j+1,a[i])
                break ##### Haha easy fix! literally anyhow haha
        j=j+1         
i=i+1


print(b)
