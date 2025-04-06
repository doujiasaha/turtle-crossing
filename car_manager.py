from turtle import Turtle
import random,time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAX_CARS = 20


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_amount = []
        self.current_speed = STARTING_MOVE_DISTANCE


    def spawn(self):
        y_positions = list(range(-250,280,10))
        random_y = random.choice(y_positions)
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(1,2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.seth(180)
        new_car.goto(300, random_y)
        self.car_amount.append(new_car)

    def check_amount(self):
        while len(self.car_amount) < MAX_CARS:
            self.spawn()            
            
    def car_movement(self):
        for car in self.car_amount:
            car.forward(self.current_speed)
            
    def difficulty(self):
        self.current_speed += MOVE_INCREMENT

"""
2. Cars are randomly generated along the y-axis and 
will move from the right edge of the screen to the left edge.
3. When the turtle hits the top edge of the screen, 
it moves back to the original position and the player levels up.
On the next level, the car speed increases.
"""