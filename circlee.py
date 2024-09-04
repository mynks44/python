import math

user_input = input("Enter radius and perimeter value separated by ;: ")

rad, pi = map(float, user_input.split(";"))

if rad <= 0 or pi <= 0:
    print("Error: Both rad and pi value must be greater than 0.")
else:
    area = pi * rad ** 2
    perimeter = 2 * pi * rad

    print(f"Area: {area:.2f}")
    print(f"Perimeter: {perimeter:.2f}")