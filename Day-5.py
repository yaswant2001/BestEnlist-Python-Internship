def calculator(num1,num2):
    sum=num1+num2
    sub=num1-num2
    mul=num1*num2
    div=num1/num2
    print("Addition of two numbers is", sum)
    print("Subtraction of two numbers",sub)
    print("Multiplication of two numbers", mul)
    print("Division of two numbers",div)

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
calculator(num1,num2)

def covid(name,body_temp=98):
    print("name:"+name,"body temperature:",body_temp)
covid("yash",98.5)
covid("yash")