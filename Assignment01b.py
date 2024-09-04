import random
import math

class Righttriangle:
    #constant variable 2.0
    POWER = 2.0
    
    def __init__(self):
    #it will choose random numbers between 0 to 6
        self.base = random.uniform(0, 6)
        self.height = random.uniform(0, 6)
    
    #pythagores theoram for hypotenuse 
    def compute_hypotenuse(self):
        hypotenuse = math.sqrt(math.pow(self.base, self.POWER) + math.pow(self.height, self.POWER))
        return hypotenuse
    
    #Compute the hypotenuse
    def display_values(self):
        hypotenuse = self.compute_hypotenuse()
        #it will print base, height and hypotenuse on the screen 
        print(f"Base    : {self.base:.2f}")
        print(f"Height  : {self.height:.2f}")
        print(f"Hypotenuse: {hypotenuse:.2f}")

triangle = Righttriangle()
triangle.display_values()
