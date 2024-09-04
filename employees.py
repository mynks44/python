ne = int(input("Enter the number of employees: "))

employeec = 1

while employeec <= ne:
    sales = float(input(f"Enter the monthly sales for employee {employeec}: "))
    
    if sales > 10000:
        print(f"qualifies for a day off")
    
    employeec += 1
