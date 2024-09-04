import math

def calccyl(rad, hei):
    vol = math.pi * (rad ** 2) * hei
    surfacearea = 2 * math.pi * rad * (rad + hei)
    return vol, surfacearea

def compareCylinders(vol, surfacearea):
    return vol > surfacearea

def main():
    cylinders = []

    for i in range(6):
        name = input(f"Enter the name of cylinder {i+1}: ")
        
        while True:
            try:
                vol = float(input(f"Enter the volume of cylinder {i+1}: "))
                surfacearea = float(input(f"Enter the surface area of cylinder {i+1}: "))
                if vol <= 0 or surfacearea <= 0:
                    print("vol and surface area must be positive numbers. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter numerical values for vol and surface area.")
        
        cylinders.append((name, vol, surfacearea))
    
    for name, vol, surfacearea in cylinders:
        print(f"\nCylinder Name: %s" % name)
        print("vol: %.2f" % vol)
        print("Surface Area: %.2f" % surfacearea)
        
        if compareCylinders(vol, surfacearea):
            print("vol is greater than Surface Area")
        else:
            print("vol is not greater than Surface Area")

if __name__ == "__main__":
    main()
