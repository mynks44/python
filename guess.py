import random

def main():
    n = int(input("Enter the maximum range value n for guessing the number: "))
    
    secretnumber = random.randint(1, n)
    
    print(f"Guess the number between 1 and {n}. Enter 0 or a negative number to quit.")
    
    while True:
        guess = int(input("Enter your guess: "))
        
        if guess <= 0:
            print("You chose to exit the game. Goodbye!")
            break
        
        if guess < secretnumber:
            print("Your guess is too low.")
        elif guess > secretnumber:
            print("Your guess is too high.")
        else:
            print("Congratulations! You've guessed the correct number.")
            break

if __name__ == "__main__":
    main()
