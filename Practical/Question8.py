#PROGRAM TO SWAP TWO NUMBWE WITHOUT TAKING ADDITIONAL VARIABLE
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
print("Number before swapping are:",x,y)
x=x+y
y=x-y
x=x-y
print("Number after swapping are:",x,y)
