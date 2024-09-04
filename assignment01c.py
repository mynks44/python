#question1
import math
a = 2
b = 3
c = -4
discriminant = b**2 - 4*a*c

if discriminant >= 0:
    sqrt_discriminant = math.sqrt(discriminant)
    root1 = (-b + sqrt_discriminant) / (2*a)
    root2 = (-b - sqrt_discriminant) / (2*a)
    print("This program computes the roots of a quadratic equation.")
    print(f"The roots are {root1:.2f} and {root2:.2f}")
else:
    print("The equation has no real roots.")
print("\n")


#question2
print("This program calculates the distance between two points.")
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"The distance between the two points is {distance:.2f}")
print("\n")

#question3
print("This program computes the volume and surface area of a sphere.")

radius = float(input("Please enter the radius of the sphere: "))

volume = (4/3) * math.pi * math.pow(radius, 3)
surface_area = 4 * math.pi * math.pow(radius, 2)

print(f"The volume is {volume:.2f} cubic units.")
print(f"The surface area is {surface_area:.2f} square units.")
