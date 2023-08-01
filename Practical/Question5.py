print("Enter the value of a,b and c for equation ax**2+bx+c")
a=int(input("Enter the value of a:"))
b=int(input("ENter the value of b:"))
c=int(input("Enter the value of c:"))
d=(b**2)-4*a*c
if (d>=0):
    print("The roots of the quadratic equation are Real")
else:
    print("The roots of the quadratic equation are Imaginary")
    

