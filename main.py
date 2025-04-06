import time, random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(player.up, "w")

spawn_timer = 0
next_spawn_time = random.uniform(0, 1)

game_is_on = True
while game_is_on:
    #check for real time
    current_time = time.time()

    #move all cards
    cars.car_movement()

    #check if enough time (0 to 1 second) has passed since last car has spawned and if yes, spawn a new car.
    #when less than 20 cars > spawn a car on the right edge.
    if current_time - spawn_timer > next_spawn_time:
        if len(cars.car_amount) < 20:
            cars.spawn()
            spawn_timer = current_time
            next_spawn_time = random.uniform(0, 1)
    
    #if car is out of screen, remove element from list.
    for car in cars.car_amount[:]:
        if car.xcor() < -320:
            cars.car_amount.remove(car)

    #collision with car onto turtle
    for car in cars.car_amount:
        if player.distance(car) < 20:
            print("HIT")
            game_is_on = False
    
    #game-winning logic
    if player.ycor() > 280:
        player.finish()
        score.level_up()
        cars.difficulty()
        print(f"current speed is {cars.current_speed}")
    
    time.sleep(0.1)
    screen.update()


"""
1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.

2. Cars are randomly generated along the y-axis and 
will move from the right edge of the screen to the left edge.
3. When the turtle hits the top edge of the screen, 
it moves back to the original position and the player levels up.
On the next level, the car speed increases.

4. When the turtle collides with a car, it's game over and everything stops.
"""