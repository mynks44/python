def main():
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))

    if abs(numerator) < abs(denominator):
        print(f"{numerator} / {denominator} is a proper fraction")
    else:
        integerp = numerator // denominator
        remainder = numerator % denominator
        
        if remainder == 0:
            print(f"{numerator} / {denominator} is an improper fraction and it can be reduced to {integerp}")
        else:
            print(f"{numerator} / {denominator} is an improper fraction and its mixed fraction is {integerp} + {remainder} / {denominator}")

if __name__ == "__main__":
    main()
