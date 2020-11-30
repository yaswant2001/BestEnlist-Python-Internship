#firstchallenge
#List down all the error types
#1.)NameError
#2.)ModuleNotFoundError
#3.)IndexError
#4.)ZeroDivisionError
#5.)ValueError


try:
    raise NameError('Aeroplane')
except NameError:
    print("The exception demolished")

#ModuleNotFoundError
try:
    import numpy
    print("Module found")
except:
    print("module not found")

#Indexerror
L=list(range(0,10))
try:
    print(L[30])
except:
    print("Error handled")

#ZeroDivisionError
try:
    c=9/0
    print(c)
except:
    print("Cannot divide by zero")

#ValueError
try:
    x=int(input("Enter the number"))

except:
    print("It is not a number")

#Excercise_2_Design a simple calculator app with try and except for all use cas-es
a=int(input("Enter the first integer"))
b=int(input("Enter the second integer"))
print("Choose the arithmetic function you want to do")
print("1.Addition")
print("2.Subraction")
print("3.Multiplication")
print("4.Division")
ch=int(input("Enter your choice"))
try:
    if (ch == 1):
        c = a + b
        print("The added value is: ",c)
except:
    print("Invalid input")
try:
    if(ch==2):
        c=a-b
    print("The subtracted value is: ",c)
except:
    print("Invalid input")
try:
    if(ch==3):
        c=a*b
    print("The multiplied value is: ",c)
except:
    print("Invalid input")
try:
    if(ch==4):
        c=a/b
    print("The divided value is: ",c)
except:
    print("Invalid input")
finally:
    print("End of program")

#Excercise_3_print one message if the try block raises a NameError and another for other errors
try:
    raise NameError("Apple")
except NameError:
    print("The Exception is handled")

#Excercise_4_When try-except scenario is not required
#Answer:Whwenever there is no need for error to be handled or we can let the program to display the error,try-except scenario is not required.

#Excercise_5_Try getting an input inside the try catch block
while True:
    try:
        t=int(input("Enter the integer"))
        print("The integer you have entered is",t)
        break
    except:
        print("Invalid integer")
print("Yeah!!,Successfully you have entered integer")