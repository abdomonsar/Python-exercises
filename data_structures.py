#Create an empty list and add items to it:
my_list=[]
co=int(input("Enter Number list: "))
for i in range(co):
    item=input(f"Enter item {i+1}")
    my_list.append(item)
print(my_list)    
#Accessing menu items
name=["A","B","C"]
print(name[0])
print(name[-1])
#Modify an item in a list
fruits = ["Apple", "Banana", "Orange"]
fruits[2]="Mango"
print(fruits)
#Delete an item from a list
fruits = ["Apple", "Banana", "Orange"]
fruits.remove("Apple")
print(fruits)
#Merge two lists
list1 = ["Apple", "Banana"]
list2 = ["Orange", "Mango"]
mar=list1 + list2
print(mar)
#Sort a list of numbers
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
#Find the largest and smallest item in a list (using built-in functions):
numbers = [5, 2, 9, 1, 7]
print(max(numbers))
print(min(numbers))
#No duplicates of an item in a list
count=0
numbers = [5, 2, 2, 1, 7]
for i in numbers:
    if i==2:
        count+=1
print(count)        
#Create a submenu (Slicing):
menu = ["Burger", "Pizza", "Juice", "Salad", "Fries", "Water"]
sub=menu[1:4]
print(sub)
#Remove an item from a specific location in a list:
my_list = ["Apple", "Banana", "Orange", "Mango"]
my_list.pop(2)
print(my_list)
#Clear all list items:
my_list = ["Apple", "Banana", "Orange", "Mango"]
my_list.clear()
print(my_list)