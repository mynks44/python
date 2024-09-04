def calcdisc(custtype, subtotal):
    discper = 0

    if custtype == 'R':
        if subtotal >= 250:
            discper = 25
        elif subtotal >= 100:
            discper = 10
        else:
            discper = 0
    elif custtype == 'C':
        if subtotal >= 250:
            discper = 30
        else:
            discper = 20
    else:
        discper = 0

    return discper

def main():
    for i in range(5):
        print(f"\nCustomer {i+1}:")
        
        while True:
            custtype = input("Enter customer type: R for Regular, C for Corporate: ").strip().upper()
            if custtype not in ['R', 'C']:
                print("Invalid customer type. Please enter 'R' for Regular or 'C' for Corporate.")
            else:
                break
        
        while True:
            try:
                subtotal = float(input("Enter the subtotal amount: "))
                if subtotal < 0:
                    print("Subtotal must be a non-negative number. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numerical value for subtotal.")
        
        discper = calcdisc(custtype, subtotal)
        discount_amount = (discper / 100) * subtotal
        total = subtotal - discount_amount
        
        print("Customer Type: %s" % custtype)
        print("Subtotal: %.2f" % subtotal)
        print("Discount Percent: %d%%" % discper)
        print("Discount Amount: %.2f" % discount_amount)
        print("Total: %.2f" % total)

if __name__ == "__main__":
    main()
