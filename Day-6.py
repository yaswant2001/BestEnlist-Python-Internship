#firstchallenge
list1=[1,2,3,4,5]
list2=[x+2 for x in list1]
print(list2)
#secondchallenge
n=5
for i in range(n,0,-1):
    j=i
    while(j > 0):
        print(j,end="")
        j=j-1
    print()
#thirdchallenge
num=int(input("enter value for num:"))
n1,n2=0,1
count=0
if(num<=0):
    print("error! needs positive number")
elif(num==1):
    print(n1)
else:
    while(count<num):
        print(n1," " ,end="")
        n=n1+n2
        n1=n2
        n2=n
        count+=1
#fourthchallenge
num=int(input("enter num:"))
sum=0
temp=num
while(temp>0):
    d=temp%10
    sum+=d ** 3
    temp //=10
if(num==sum):
    print("number is armstrong number")
else:
    print("not an armstrong number")
#fifthchallenge
for i in range (1,11):
    print(9,'x',i,'=',9*i)
#sixthchallenge
num=int(input("enter a number:"))
if(num>=0):
    print("positive number")
else:
    print("negative number")
#seventhchallenge
days=int(input("enter days:"))
years=days//365
print("age is:",years)
#8challenge
import math
res=math.cos(30)**2+math.cos(30)**2

print(res)
#9challenge
num1=float(input("enter num1:"))
num2=float(input("enter num2:"))
res=0
operator=input("enter operator:")

if(operator=="+"):
    res=num1+num2
if(operator=="-"):
    res=num1-num2
if(operator=="*"):
    res=num1*num2
if(operator=="/"):
    res=num1/num2
print("output:",res)