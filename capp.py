def calct(stotal, custype):
    if stotal < 0:
        return "Invalid subtotal amount. It must be greater than or equal to 0."
    
    dispercent = 0
    
    if custype == 'R':
        if stotal >= 250:
            dispercent = 25
        elif stotal >= 100:
            dispercent = 10
    elif custype == 'C':
        if stotal >= 250:
            dispercent = 30
        else:
            dispercent = 20
    else:
        return "No discount for this stotal"
    
    disamount = stotal * (dispercent / 100)
    tamount = stotal - disamount
    return tamount

for i in range(5):
    while True:
        try:
            stotal = float(input(f"Enter the subtotal for customer {i+1}: "))
            if stotal < 0:
                raise ValueError("subtotal must be greater than or equal to 0.")
            break
        except ValueError as e:
            print(e)
    
    custype = input(f"Enter the customer type for customer {i+1} : ").upper()
    
    total = calct(stotal, custype)
    print(f"Total amount for customer {i+1}: {total}\n")
