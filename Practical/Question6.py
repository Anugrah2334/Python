print("PROGRAM TO FIND WHETHER THE GIVEN YEAR IS LEAP YEAR OR NOT")
x=int(input("Enter the year you want to search:"))
if x%4==0 or x%400==0 and x%100!=0:
    print("The entered year is a Leap year")
else:
    print("The entered year is not a Leap year")
