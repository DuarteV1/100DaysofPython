import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Global variables
game_is_on = True
game_speed = 0.1

screen = Screen()
# Screen definitions and methods
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Objects
player = Player()
score = Scoreboard()
car = CarManager()
screen.onkeypress(key="Up", fun=player.move_up)

# While loop
while game_is_on:
    time.sleep(game_speed)
    screen.update()

    car.create_car()
    car.move_left()

    # Level Up - Detect collision with a y-cor and adds score
    if player.is_at_finish_line():
        score.level_up()
        car.speed_up_cars()
        player.goto(0, -280)

    # GAME OVER - Detects collision with a car
    for cars in car.list_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()
