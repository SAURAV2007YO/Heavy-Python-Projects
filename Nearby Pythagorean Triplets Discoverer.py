print("Enter the Desired Positive Integer (A); for checking Pythagorean Triplets")
print("in Which 2 Numbers are in the range A-100 to A+100")

a= int(input("Enter Number for Checking Nearby Pythagorean Triplets: "))

if (a>=101):
    b = range(a-100, a+101)
else:
    b= range(1, a+101)


if (a>=1):
    for i in b:
        for j in b:
            if (i>j):
                d = ((i**2) + (j**2))**(0.5)
                if (d-int(d)==0):
                    print(i,j,int(d))
        j=j+1
    i = i+1
else:
    print("Non Positive Integers are not part of pythagorean Triplets")

z = input()
print(z)
