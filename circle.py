import math

def calcarea(radius):
    return math.pi * radius ** 2

def calcperi(radius):
    return 2 * math.pi * radius

def main():
    ui = input("Enter the radius of the circle: ").strip()
    
    try:
        radius_str = ui.split(';')[0]
        radius = float(radius_str)
    except (ValueError, IndexError):
        print("please enter atleaaest one number")
        return
    
    area = calcarea(radius)
    perimeter = calcperi(radius)
    
    print(f"Area: {area:.2f}")
    print(f"Perimeter: {perimeter:.2f}")

if __name__ == "__main__":
    main()
