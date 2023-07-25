#object_name=class_name()
#object_name.class_member_name

class ABC:
    var=10
obj=ABC()
print(obj.var)

class Sample:
    x,y=10,20
S=Sample()
print('Value of x=', S.x)
print('Value of y=', S.y)
print('Value of x and y=', S.x+S.y)

class ABC():
    var=10
    def display(self):
        print('In class method.....')
obj=ABC()
print(obj.var)
obj.display()

class student:
    mark1, mark2, mark3=45,91,71
    def process(self):
        sum=student.mark1+student.mark2+student.mark3
        avg=sum/3
        print('Total Marks=', sum)
        print('Average marks=', avg)
        return
s=student()
s.process()


class odd_even:
    even=0
    def check (self, num):
        if num%2==0:
            print(num, 'is even number')
        else:
            print(num, 'is odd number')
n=odd_even()
x=int(input('Enter the value:'))
n.check(x)
