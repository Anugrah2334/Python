#PROGRAM1 (keyword argument)
def my_function(child3,child2,child1):
    print("The youngest child is" +child3)
my_function(child1="Emil",child2="Tobais",child3="Linus")
print("\n")

#PROGRAM2 (variable-length argument)
def func(name, *fav_subjects):
    print("\n", name, " likes to read")
    for subject in fav_subjects:
        print(subject)
func("Goransh", "Mathematics", "Android Programming")
func("Richa", "C", "Data Structures", "Design and Analysis of Algorithms")
func("Krish")
print("\n")

def my_function(*kids):
    print("The youngest child is "+kids[2])
my_function("Emil", "Tobais", "Linus")
print("\n")

#PROGRAM3 (Arbitrary keyword argument)
def my_function(**kid):
    print("His last name is "+ kid["lname"])
my_function(fname="Tobais", lname="Refsnes")
print("\n")

#PROGRAM4 (Default Arguments)
def display(name, course= "BTech"):
    print("Name :"+name)
    print("Course :",course)
display(course= "BCA", name="Arav") #keyword argument
display(name= "Reyansh")            #default argument for course
print("\n")

def my_function(country= "Norway"):
    print("I am from "+country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
print("\n")

#PROGRAM5 (Passing list as an argument)
def my_function(food):
    for x in food:
        print(x)
fruits=["apple", "banana", "cherry"]
my_function(fruits)
print("\n")

#PROGRAM6 (Lambda Functions or Anonymous Function)
sum=lambda x,y: x+y
print("Sum= ",sum(3,5))
print("\n")

x=lambda a:a+10
print(x(5))
print("\n")

x=lambda a,b:a*b
print(x(5,6))
print("\n")

x=lambda a,b,c: a+b+c
print(x(5,6,2))
print("\n")

def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(11))
print("\n")

def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(3)
print(mydoubler(11))
print("\n")

def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
mytripler=myfunc(3)
print(mydoubler(11))
print(mytripler(11))
print("\n")

str1='GeeksforGeeks'
#lambda returns a function object
rev_upper=lambda string:string.upper()[::-1]
print(rev_upper(str1))








    



