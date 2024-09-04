def rectanglepoint(x, y, rectx, recty, rectw, recth):
    hw = rectw / 2
    hh = recth / 2
    
    if (rectx - hw <= x <= rectx + hw) and (recty - hh <= y <= recty + hh):
        return True
    else:
        return False

def main():
    x, y = map(float, input("Enter a point with two coordinates: ").split())
    
    rectx = 0
    recty = 0
    rectw = 10
    recth = 5
    
    if rectanglepoint(x, y, rectx, recty, rectw, recth):
        print(f"Point ({x}, {y}) is in the rectangle")
    else:
        print(f"Point ({x}, {y}) is not in the rectangle")

if __name__ == "__main__":
    main()
