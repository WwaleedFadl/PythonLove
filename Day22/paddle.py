from turtle import Turtle

SHAPE = 'square'
COLOR = 'white'
WIDTH=5
LENGTH=1 
STARTING_POSITION=(350,0)

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(WIDTH,LENGTH)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
