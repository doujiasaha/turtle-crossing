from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.score = 1
        self.level()
        
    def level(self):
        self.goto(-220,260)
        self.write(f"Level: {self.score}", True, "center", font=FONT)
        
    def level_up(self):
        self.score += 1
        self.clear()
        self.level()
