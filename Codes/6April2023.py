class ABC():
    var=10
    def display(self):
        print('In class method....')
obj=ABC()
print(obj.var)
obj.display()

class student:
    mark1, mark2, mark3=45,91,71
    def process(self):
        sum=student.mark1+student.mark2+student.mark3
        avg=sum/3
        print('total marks=', sum)
        print('Average marks=', avg)
        return
s=student()
s.process()

class ABC():
    def __init__(self, val):
        print('In class method.....')
        self.val=val
        print('The value is :', val)
obj=ABC(10)

class sample:
    def __init__(self, num):
        print('Constructor of sample class')
        self.num=num
        print('The value is:', num)
s=sample(10)

class ABC():
    class_var=0
    def __init__(self, var):
        ABC.class_var+=1
        self.var=var
        print('The object value is:', var)
        print('The value of class variable is:', ABC.class_var)
obj1=ABC(10)
obj2=ABC(20)
obj3=ABC(30)

class sample:
    num=0
    def __init__(self, var):
        sample.num+=1
        self.var=var
        print('the object  value is :', var)
        print('the count of the object created :', sample.num)
s1=sample(15)
s2=sample(35)
s3=sample(45)

class ABC():
    class_var=0
    def __init__(self, var):
        ABC.class_var+=1
        self.var=var
        print('the object value is :', var)
        print('The value of the class variable is :', ABC.class_var)
    def __del__(self):
        ABC.class_var-=1
        print('object with value %d is going out of scope'%self.var)
obj1=ABC(10)
obj2=ABC(20)
obj3=ABC(30)
del obj1
del obj2
del obj3

class sample:
    num=0
    def __init__(self, var):
        sample.num+=1
        self.var=var
        print('The object value is:', var)
        print('The values of class variable is:', sample.num)
        def __del__(self):
            sample.num=1
            print('Object with value %d is exit from the scope'%self.var)
s1=sample(15)
s2=sample(35)
s3=sample(35)

class ABC():
    def __init__(self, name, var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self, obj):
        return self.var - obj.var
obj =ABC('abcdef', 10)
print('The value stored in object is:', repr(obj))
print('The length of name stored in object is:', len(obj))
obj1=ABC('ghijkl', 1)
val=obj.__cmp__(obj1)
if val==0:
    print('Both values are equal')
elif val==1:
    print('First value is less than second')
else:
    print('Second value is less than first')


class ABC():
    def __init__(self, var1, var2):
        self.var1=var1
        self.__var2=var2
    def display(self):
        print('From class method, var1=', self.var1)
        print('From class method, var12=', self.__var2)
obj=ABC(10, 20)
obj.display()
print('From the main module, var1=', obj.var1)
print('From the main module, var2=', obj.__var2)

class sample:
    def __init__(self, n1, n2):
        self.n1=n1
        self.__n2=n2
    def diplay(self):
        print('Class variable1=', self.n1)
        print('Class variable2=', self.__n2)
s=sample(12,14)
s.display()
print('Value 1=', s.n1)
print('Value 2=', s.__n2)

#write a program to calculate area and circumference of a circle

class circle:
    pi=3.14
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return circle.pi*(self.radius**2)
    def circumference(self):
        return circle.pi*self.radius*2
r=int(input('Enter the radius'))
c=circle(r)
print('Area:', c.area())
print('Circumference:', c.circumference())

#write a menu driven program that keeps record of books available in your school

class libary:
    def __init__(self):
        self.bookname=''
        self.author=''
    def getdata(self):
        self.bookname=input('Enter the name of the book:')
        self.author=input('Enter author of the book:')
    def display(self):
        print('Name of the book:', self.bookname)
        print('author name of book:', self.author)
        print('\n')
book=[]
ch='y'
while(ch=='y'):
    print('1.Add new book \n2.Display books')
    resp=int(input('Enter your choice:'))
    if (resp==1):
        l=libary()
        l.getdata()
        book.append(l)
    elif(resp==2):
        for x in book:
            x.display()
    else:
        print('Invalid input.....')
    ch=input('Do you want continue....')

#write a program to accept a string and print the number of 
#uppercase, lowercase, vowels, consonants and spaces in the 
#given string

class string:
    def __init__(self):
        self.uppercase=0
        self.lowercase=0
        self.vowels=0
        self.consonants=0
        self.spaces=0
        self.string=''
    def getstr(self):
        self.string=str(input('Enter a string:'))
    def count_upper(self):
        for ch in self.string:
            if (ch.isupper()):
                self.uppercase+=1
    def count_lower(self):
        for ch in self.string:
            if (ch.islower()):
                self.lowercase+=1
    def count_vowels(self):
        for ch in self.string:
            if (ch in 'A','a','E','e','I','i','O','o','U','u'):
                self.vowels+=1
    def count_consonants(self):
        for ch in self.string:
            if (ch not in 'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'):
                self.consonants+=1
    def count_space(self):
        for ch in self.string:
            if (ch==' '):
                self.spaces+=1
    def execute(self):
        self.count_upper()
        self.count_lower()
        self.count_vowels()
        self.count_consonants()
        self.count_space()
    def display(self):
        print('The given string contains:')
        print('%dUppercase letters'%self.uppercase)
        print('%dLowercase letters'%self.lowercase)
        print('%dVowels'%self.vowels)
        print('%dConsonants'%self.consonants)
        print('%dSpaces'%self.spaces)
s=string()
s.getstr()
s.execute()

#write a program to store product and its cost price.Display all 
#available products and prompt to enter quantity of all products.
#finally generate a bill which displays the total amount to be paid

class mystore:
    __prod_code=[]
    __prod_name=[]
    __prod_price=[]
    __prod_quant=[]
    def getdata(self):
        self.p=int(input('Enter number of product you need to store:'))
        for x in range(self.p):
            self.__prod_code.append(int(input('Enter the product code:')))
            self.__prod_name.append(str(input('Enter product name:')))
            self.__prod_price.append(int(input('Enter the price of product:')))
    def display(self):
        print('Stock in stores')
        print('-----------------------------')
        print('Product code \t Product Name \t Cost price')
        print('---------------------------------------')
        for x in range(self.p):
            print(self.__prod_code[x], '\t\t', self.__prod_price[x])   
        print('----------------------------------------')   
    def print_bill(self):
        total_price=0
        for x in range(self.p):
            q=int(input('Enter the quantity for product code %d:'%self.__prod_code[x]))
            self.__prod_quant.append(q)
        total_price=total_price+self.__prod_price[x]*self.__prod_quant[x]
        print('Invoice Receipt')
        print('----------------------------------')
        print('Product Code \t Product Name \t Cost price \tQuantity \t Total Amount')
        print('---------------------------------------------')
        for x in range(self.p):
            print(self.__prod_code[x], '\t\t', self.__prod_name[x], '\t\t', self.__prod_price[x], '\t\t', self.__prod_quant[x], '\t\t', self.__prod_quant[x]*self.__prod_price[x])
            print('-------------------------------------------')
        print('Total Amount=', total_price)
s=mystore()
s.getdata()
s.display()
s.print_bill()

class ABC():
    def __init__(self, var):
        self.__var=var
    def __display(self):
        print('From class method, var:', self.__var)
obj=ABC(10)
obj._ABC__display()

class ABC():
    def __init__(self, var):
        self.var=var
    def display(self):
        print('Var is :', self.var)
    def add_2(self):
        self.var+=2
        self.display()
obj=ABC(10)
obj.add_2()

class ABC():
    def __init__(self, var):
        self.var=var
    def display(self):
        print('Var is:', self.var)
obj=ABC(10)
obj.display()
print('Check if the object has attribute....', hasattr(obj, 'var'))
getattr(obj, 'var')
setattr(obj, 'var', 50)
print('After setting value , var is :', obj.var)
setattr(obj, 'count', 10)
print('New variable count is created and its value is:', obj.count)
delattr(obj, 'var')
print('After deleting the attribute, var is :', obj.var)

class ABC():
    def __init__(self, var1, var2):
        self.var1=var1
        self.var2=var2
    def display(self):
        print('Var1 is :', self.var1)
        print('Var2 is :', self.var2)
obj=ABC(10, 12, 34)
obj.display()
print('Object.__dict__:', obj.__dict__)
print('object.__doc__:', obj.__doc__)
print('class.__name__:', ABC.__name__)
print('object.__module__:', obj.__module__)
print('class.__bases__:', ABC.__bases__)
