"Import the turtle class from the turtle module"
"""Create constants for the starting position of the snakes, speed they
will move and the angles they should turn when pressed up, down, left, and right"""
from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

"Create the snakes class"
class Snakes:

    "Create lists that will store the segments, create the snakes and initialize the head of the snakes"
    def __init__(self, snake_info):
        self.color = snake_info['color']
        self.starting_position = snake_info['starting_position']
        self.segments = []
        self.create_snake(self.starting_position, self.color)
        self.head = self.segments[0]

    "Create the snake using the starting_positions data"
    def create_snake(self, starting_position, color):
        for position in starting_position:
            self.add_segment(position, color)

    "Here is where the details of the snake are created: location, shape, color"
    "Penup will allow it to not create a continuous line and goto will move it to the specified destination"
    def add_segment(self, position, color):
        new_segment = Turtle("square")
        new_segment.color(color)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    "Extend the tail of the snake"
    def extend(self):
        self.add_segment(self.segments[-1].position(), self.color)  

    """A certain algorithm is used to move the snake accordingly. Second shape will move to the first, 
    the third to the second etc. and finally the head will move to the newest angle"""
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    #Up, Down, Left, Right Movements for 1st Snake        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)