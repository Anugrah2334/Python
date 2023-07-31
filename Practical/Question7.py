#TO CONVERT GIVEN SECOND INTO HOUR, MINUTE AND REMANING SECOND
x=int(input("Enter time in seconds:"))
hour=x//3600;
rem=x%3600
min=rem//60
sec=rem%60
print(hour,"hours",min,"minutes",sec,"seconds")
