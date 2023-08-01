d=int(input("Enter the day:"))
m=int(input("Enter the month:"))
y=int(input("Enter the year:"))
k=d+1
l=1
j=[1,3,5,7,8,10]
o=[4,6,9,11]
if(k==32 and m in j):
    print(l,m+1,y)
elif(k==31 and m in o):
    print(l,m+1,y)
elif(k==28 and m==2):
    print(l,m+1,y)
elif(k==32 and m==12):
    print(l,l,y+1)
else:
    print(d,m,y)
