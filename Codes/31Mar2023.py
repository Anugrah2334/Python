#else clause
try:
    file=open('File1.txt')
    str=file.readline()
    print(str)
except IOError:
    print('Error occurred during Input.....Program Terminating....')
else:
    print('Program Terminating Successfully....')

try:
    num=10
    print(num)
    raise ValueError
except:
    print('Exception occurred .....Program Terminating...')

#instantiating Exceptions
try:
    raise Exception('Hello', 'World')
except Exception as errorObj:
    print(type(errorObj))
    print(errorObj.args)
    print(errorObj)
    arg1, arg2=errorObj.args
    print('Argument1=', arg1)
    print('Argument2=', arg2)

#handling exception in invoked function
def Divide(num, demo):
    try:
        quo=num/demo
        print(quo)
    except ZeroDivisionError:
        print('You cannot divide a number by zero ... Program Terminating...')
Divide(10, 0)

#finally block
try:
    print('Raising Excepion...')
    raise ValueError
finally:
    print('Performing clean up in Finally....')

#pre-defined clean up action
with open('File1.txt') as file:
    for line in file:
        print(line)

#re-rasing exception
try:
    f=open('Abc123.txt')
except:
    print('File does not exist')
    raise  #re-raise the caught exception

#assertion
c=int(input('ENter the temperature in Celcius'))
f=(c*9/5)+32
assert(f<=32), 'Its freezing'
print('Temperature in Fahrehnit:')
