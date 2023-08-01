name = input("Enter you name : ")
roll_no = input("Enter your Roll number : ")
sap_id = int(input("Enter your SAP ID : "))
sem = input("Enter your semseter : ")
Course = input("Enter your course name : ")

PDS = int(input("Enter your marks of PDS : "))
python = int(input("Enter your marks of python : "))
chem = int(input("Enter your marks of chemistry : "))
eng = int(input("Enter your marks of english : "))
phy = int(input("Enter your marks of physics : "))

print("Name : " + name )
print("Roll Number : " + roll_no + "\t \t SAP ID : ",sap_id)
print("Sem : " + sem + "\t \t Course : " + Course)
print("\n")
print("Subject name : Marks ")
print("PDS          : ",PDS)
print("Python       : ",python)
print("Chemsitry    : ",chem)
print("English      : ",eng)
print("Physics      : ",phy)
per= float((PDS+python+chem+eng+phy)/500)*100
print("Percentage :",per)
cgpa = float(per/10)
print("CGPA :",cgpa)

if(cgpa>=0 and cgpa<=3.4):
             print("Grade : F")
elif(cgpa>=3.5 and cgpa<=5):
             print("Grade : C+")
elif(cgpa>=5.1 and cgpa<=6):
             print("Grade : B")
elif(cgpa>=6.1 and cgpa<=7):
             print("Grade : B+")
elif(cgpa>=7.1 and cgpa<=8):
             print("Grade : A")
elif(cgpa>=8.1 and cgpa<=9):
             print("Grade : A+")
elif(cgpa>=9.1 and cgpa<=10):
             print("Grade : O") 
         
