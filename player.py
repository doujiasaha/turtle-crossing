from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.seth(90)
    
    def up(self):
        self.forward(MOVE_DISTANCE)
        
    def finish(self):
        self.goto(STARTING_POSITION)