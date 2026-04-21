import random
number=int(input("Enter Number: "))
if number ==0 :
    print(f"The Number={number}")
elif number > 0:
    print(f"The Number {number} is Positive")   
elif number <0 :
    print(f"The Number {number} is negative")   
else:
    print("Invalid entry")
num=int(input("Enter Number: "))
if num % 2 ==0:
    print(f"The Number {num} is Even")
else:
    print(f"The Number {num} is negative")    
age=int(input("Enter Your Age: "))
if age >= 18 :
    print("Eligible to vote")
else :
    print("Not eligible to vote")    

number1=int(input("Enter Number1: "))
number2=int(input("Enter Number2: "))  
result=f"{number1} > {number2}" if number1 > number2 else f"{number2} > {number1}"  
print(result)   
number1=int(input("Enter Number1: "))
number2=int(input("Enter Number2: "))    
number3=int(input("Enter Number3: "))
if number1 > number2 and number1 > number3:
    print(number1)
elif number2 > number1 and number2 > number3 :
    print(number2)
else:
    print(number3)        
degree=int(input("Enter degree: "))
if degree >=90 :
    print("A")
elif degree >=80 and degree <90:
    print("B")
elif degree >=70 and degree <80:
    print("C")  
elif degree >=60 and degree <70:
    print("D")    
else:
    print("F")    
ch = input("Enter a letter: ")
if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")   
passwod=(input("Enter PassWor:"))
result= "True" if passwod=="password123" else "False"  
print(result)   
age=int(input("Enter Age: "))
if age <= 16 :
    print("The ticket is free")
elif age > 16 and age <40 :
    print("Full price")   
else :
    print("descount")     
num=float(input("Enter Number: "))
if 10 <= num >=20 :
    print("The number is within the range")
else :
    print("The number is not within the range")  
num1=float(input("Enter number 1: "))  
num2=float(input("Enter number 2: ")) 
if num1 == num2 :
    print("It equals") 
else :
    print("Not equal")    
sentence=input("Enter sentence: ")
if "python" in sentence:
    print("existing")
else :
    print("unavailable")    

numra=random.randint(1,10)
while True :
    num=int(input("Enter number between 1-10: "))
    if num == numra :
        print("I won")
        break
    elif num > numra :
        print("The number is bigger")
    else :
        print("The number is smaller")    
ch=input("Enter a character: ")
if len(ch) !=1 :
    print("Enter just one letter")
elif ch.isdigit():
    print("Number")
elif ch.islower():
    print("Small letter")   
elif ch.isupper():
    print("uppercase letter")     
else :
    print("code")     
text = input("Enter text: ")
if text.strip() !="" :
    print("The text is not empty")
    print(text)
else :
    print("The text is empty")    
username="AbdulMajeed"
password="pasword123"
user=input("Enter UserName: ")
passw=input("Enter Password: ")
if user==username and passw==password :
    print("Corecct")
else :
    print("Erorr")            