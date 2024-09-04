class bankacc:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def setn(self, name):
        self.__name = name

    def setb(self, balance):
        self.__balance = balance

    def getn(self):
        return self.__name

    def getb(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 <= amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount.")

def main():
    last_name = input("Enter the account holder's last name: ")
    start_bal = float(input("Enter the starting balance: "))

    acc1 = bankacc(last_name, start_bal)

    depositam = float(input("Enter the amount to deposit: "))
    acc1.deposit(depositam)

    withdrawam = float(input("Enter the amount to withdraw: "))
    acc1.withdraw(withdrawam)

    finalb = acc1.getb()
    print(f"Final balance: {finalb}")

if __name__ == "__main__":
    main()
