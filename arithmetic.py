import math
# 1-2-3-4-5
number1=float(input("Enter Number1: "))
number2=float(input("Enter Number2: "))
sum=number1 + number2
sub=number1 - number2
mul=number1 * number2
div=number1 / number2 if number2 !=0 else "It cannot be divided by zero"
re=number1 % number2
print(sum)
print(sub)
print(mul)
print(div)
# 6
number1=float(input("Enter Number1: "))
number2=float(input("Enter Number2: "))
ace=number1**number2
ace=pow(number1,number2)
print(ace)
# 7
number=float(input("Enter Number1: "))
number=math.sqrt(number)
print(number)
# 8
length=float(input("Enter length: "))
width=float(input("Enter width: "))
area=length*width
print(area)
# 9
r=float(input("Enter the radius: "))
area=math.pi *(r**2)
print(area)
# 10
r=float(input("Enter the radius: "))
circumference=2 * math.pi *r
print(circumference)
# 19
num=3.14159
print(round(num,2))


