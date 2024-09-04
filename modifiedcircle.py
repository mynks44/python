import math

def calcarea(radius):
    return math.pi * radius ** 2

def calcperi(radius):
    return 2 * math.pi * radius

def cir():
    ui = input("Enter the radius of the circle: ").strip()
    
    try:
        radius_str = ui.split(';')[0]
        radius = float(radius_str)
    except (ValueError, IndexError):
        print("Invalid input format. Please enter the radius in the format.")
        return None
    
    area = calcarea(radius)
    perimeter = calcperi(radius)
    
    return radius, area, perimeter

def main():
    num_circles = int(input("Enter the number of circles: "))
    
    for i in range(num_circles):
        print(f"\nFor a circle {i + 1}:")
        result = cir()
        if result:
            radius, area, perimeter = result
            print(f"Area: {area:.2f}")
            print(f"Perimeter: {perimeter:.2f}")

if __name__ == "__main__":
    main()
