from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.player = Turtle()
        self.player.shape("turtle")
        self.player.color("Black")
        self.player.penup()
        self.player.goto(STARTING_POSITION)
        self.player.seth(90)
    
    def up(self):
        self.player.forward(MOVE_DISTANCE)

    def down(self):
        self.player.back(MOVE_DISTANCE)