def main():
    tweight = 0
    count = 0

    while True:
        weight = float(input("Enter a patient's weight or 0 to stop: "))
        
        if weight == 0:
            break
        
        if weight < 0:
            print("Invalid input. Weight must be greater than 0. Please try again.")
            continue
        
        tweight += weight
        count += 1
    
    if count == 0:
        print("No weights were entered.")
    else:
        avragweight = tweight / count
        print(f"The average weight of the patients is: {avragweight:.2f}")

if __name__ == "__main__":
    main()
