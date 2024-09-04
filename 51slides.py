#22
ssn = " 392 55 7722"
ssn = ssn.strip()
print(ssn)
entry = "12345"
is_integer = entry.isdigit()
print('is',entry, ' a digit?: ', is_integer)
book = "who controls the internet?"
print(book.startwith('who'))
message = ' welcome samir to out meeting.'
print(message.title())

date = "11/9/1972"
date = date.split("/")
month = int(date[0])
day = int(date[1])
year = int(date[2])
print(month)
print(day)
print(year)

#23
a_string = 'the future depends on what we do in the present'
print(a_string)
my_string = input('enter the string you look for: ')
print(my_string, " is in ", a_string, " (true/false): ", )

#26
quotation = "these are the times that try men's souls."
words= quotation.split()
print(words[0])
print(words[3])
print(words[7])
print(words[-1])
print(words[8])

#27
adress = ["john doe","1500 any street","new york","ny","10001"]
adress = "|".join(adress)
print(adress)

#30
print("title: python programming\nquantity: 5")

print("type \"x\" to exit")
print('type \'x\' to exit')
print("type 'x' to exit")
print('type "x" to exit')

#31
print("C:\\murach\\python")
print("Title:\t\tpython programming\nquantity:\t5")

#33
name = input('enter your name: ')
greeting = 'hello, {}'.format(name)
print(greeting)

instructor = input("enter the prof's name: ")
subject = input("enter the subbject name: ")
term = input("enter the term: ")
print('{} will teach {} in {}'.format (instructor, subject, term))

#34
instructor = input("enter the prof's name: ")
subject = input("enter the subbject name: ")
term = input("enter the term: ")
print('in term: {2}, {0} will teach {1}'.format(instructor, subject, term))

#35
print('{} : {2:.2f}, {:.3f}'.format("the result: ", 2.123456, 89.1357))

#38
firstname = "raed"
lastname = 'karim'
print('%s%14s'%(firstname,lastname))

firstname = input("please, enter your first name: ")
print ('%15s'%firstname)
print ('%-15s'%firstname)

#40
print("960987392750127")
print("%-4d%10d" % (1,900))
print("%-4d%10d" % (2,9000))
print("%-4d%10d" % (3,90000))
print("%-4d%10d" % (4,900000))

print("%10d"%123)
print("-%10d"%123)
print("%-10d%-10d%-10d"%(123,456,789), end="|")

#42
x=123.45678
print("1234567890")
print('%10.2f' %x)
print('%-10.2f' %x)

print('%-15s%-15d%s%-15.1f'%('sales1',8,'$',1200.0))
print('%-15s%-15d%s%-15.1f'%('sales2',11,'$',1345.75))
print('%-15s%-15d%s%-15.1f'%('sales3',9,'$',1778.81))

#46
age = 39
print(age == 39)
print()
user_name = 'r2kar'
print(user_name = 'rkar')
print()
sales_amount = 5470.91
print(sales_amount >= 500.0)
print()
account = 'business'
print(account<0)

#49
age, city = input("enter your age and city separated with a space: ").split()
print(int(age) >= 65 and city == ' toronto')

grade = 84
passed = (grade >= 50)
print('passed: ',passed)
print('passed: ',passed)

age = 67; statues = "retired"
print(age >= 65 or age <= 18 or status == "retired")
print(age >=65 or age <= 18 or status == "retired")
print((age >= 65 and status == "retired") or age < 18)

#51
last_name = 'karin'
print(last_name.upper())
title = 'PROFESSOR'
lower_title = title.lower()
print('my title is ', lower_title)

last_name = 'karin'
print(last_name.lower() == 'karim')















