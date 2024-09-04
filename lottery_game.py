import random

def glottary():
    return random.randint(0, 99)

def clottary(lottary, ui):
    lottarys = f"{lottary:02d}"
    uistr = f"{ui:02d}"
    
    if uistr == lottarys:
        return 10000
    elif sorted(uistr) == sorted(lottarys):
        return 3000
    elif (uistr[0] in lottarys) or (uistr[1] in lottarys):
        return 1000
    else:
        return 0

def main():
    lottary = glottary()
    ui = int(input("Enter a lottary number (0-99): "))
    
    if ui < 0 or ui > 99:
        print("Invalid input. Please enter a number between 0 and 99.")
        return
    
    award = clottary(lottary, ui)
    
    print(f"The lottary number is: {lottary:02d}")
    print(f"Your input number is: {ui:02d}")
    if award == 10000:
        print("Exact match! You win $10,000!")
    elif award == 3000:
        print("Match all digits! You win $3,000!")
    elif award == 1000:
        print("Match one digit! You win $1,000!")
    else:
        print("Sorry, no match. You win $0.")

if __name__ == "__main__":
    main()