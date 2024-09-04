#6
first_name = input("enter your first name: ")
print("hello: ", first_name)

#7
score_total = 0
score = input("enter your score: ")
score_total += score

#8
hours_day1 = input("enter the hours worked in day 1: ")
hours1 = int(hours_day1)
hours_day2 = input("enter the hours worked in day 2: ")
hours2 = int(hours_day2)
total_hours = hours1 + hours2
print("the total hours worked: ", total_hours)

quantity = int(input("how many units are on the shelf?: "))
print("quantity: ", quantity)

#9
quantity = int(input("enter the quantity: "))
unit_price = float(input("enter the unit price of the product: "))
total_cost = quantity * unit_price
print("the total cost: ", total_cost)

#10
a, b=input('please enterr the two numbers to be added: ').split()
a, b = (float(a), float(b))
print ('the sum of the two numbers is:', a+b)

a, b= input('please enter the two numbers to be added').split(';')
a, b = (float(a), float(b))
print ('the sum of the two numbers is: ', a+b)

#13
first_name = "bob"
last_name = 'smith'
full_name = last_name + ", " + first_name
print("full name: ", full_name)

#15
first_name = "bob"
last_name = 'smith'
full_name = f"{last_name}, {first_name}"
print(full_name)
print()
age = 38
info = f"{last_name} is {age} years old"
print("users info: ", info)
print()
info = last_name + " is " + str(age) + " years old"
print("users info: ", info)

#16
message = "hello out there!"
message[0]
message[1]
message[-1]
print(message[0], message[1], message[-1])
message[16]

#17
message = "hello out there!"
print(message[:5])
print(message[6:9])
print(message[10:])
print(message[:-1])

#19
name = 'smir'
name = name + ' ' + 'patel'
print(name)

message = "hello out there "
message[0] = 'k'

#21
mesasge = "hello out there"
print(len(mesasge))

