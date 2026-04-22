# #Print the length of a text string
text=input("Enter Text")
print(len(text))
# #Merge two strings
text1=input("Enter Text")
text2=input("Enter Text")
print(text1 +" "+text2)
# #Duplicate a text string
text = input("Enter text: ")
count = int(input("Enter number of repetitions: "))
for i in range(count):
    print(text)
# #Convert text to uppercase and lowercase letters
text = input("Enter text: ")
print(text.upper())
print(text.lower())
# #Reverse a string
text = input("Enter text: ")
print(text[::-1])
# #Check if the text string is 
text = input("Enter text: ")
if text==text[::-1]:
      print("Palindrome")
else:
    print("Not Palindrome")
# #The number of times a character appears in text
text = input("Enter text: ")
char = input("Enter character: ")
count=text.count(char)
print(count)
# #Replace a letter with another letter in text
text = input("Enter text: ")
old_char = input("Enter letter to replace: ")
new_char = input("Enter new letter: ")
result = text.replace(old_char, new_char)
print("Result:", result)
# #Remove excess white spaces from the beginning and end of the text
text = input("Enter text: ")
clean_text = text.strip()
print("Result:", clean_text)
# #Divide text into words
text = input("Enter text: ")
words = text.split()
print(words)
#To check if text starts with "Hello"
text = input("Enter text: ")
if text.startswith("Hello"):
    print("Yes")
else :
    print("No")    
#Check if text ends with “.py”:
text = input("Enter text: ")
if text.endswith(".py"):
      print("The text ends with .py")
else:
    print("The text does NOT end with .py")
#Extracting part of the text (Slicing):
text = input("Enter text: ")
text=text[:4]
print(text)
#Convert the first letter of each word to a capital letter:
text = input("Enter text: ")
text=text.title()
print(text)
#The number of words in a sentence:
text = input("Enter a sentence: ")
words = text.split()
count = len(words)
print(count)
#Search for a specific word in text:
text = input("Enter text: ")
word = input("Enter word: ")
words =text.split()
if word in words:
    print("Word found as a full word")
else:
    print("Not found")
#Check if text contains only numbers:
text = input("Enter text: ")
if text.isdigit():
    print("Text contains only numbers")
else:
    print("Text does NOT contain only numbers")
#Check if text contains only characters:
text = input("Enter text: ")
if text.isalpha():
    print("Text contains only letters")
else:
    print("Text does NOT contain only letters")
#Convert text to a list of characters:
text = input("Enter text: ")
ch=list(text)
print(ch)









