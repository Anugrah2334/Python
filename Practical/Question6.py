#TO FIND AREA OF TRIANGLE WHEN THE LENGTH OF SIDES ARE GIVEN
x=float(input("Enter the length of 1st side:"))
y=float(input("Enter the length of 2nd side:"))
z=float(input("Enter the length of 3rd side:"))
s=(x+y+z)/2
area=(s*(s-x)*(s-y)*(s-z))**0.5
print("Area of Triangle is:",area)
