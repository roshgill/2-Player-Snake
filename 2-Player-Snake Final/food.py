"Import the turtle class from the turtle module"
from turtle import Turtle
import random

"Initialize the food class"
"Define the shape, size, and color"
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    "Everytime the food is eaten, randomize the x and y values within the screen and move it there"
    def refresh(self):
        random_x = random.randint(-335, 335)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)