from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.list_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_change = random.randint(1, 6)
        if random_change == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.starting_y = random.randint(-250, 250)
            new_car.starting_position = (300, new_car.starting_y)
            new_car.goto(new_car.starting_position)
            self.list_cars.append(new_car)

    def move_left(self):
        for car in self.list_cars:
            car.backward(self.car_speed)
        # subtract increments of 10 to STARTING_POSITION
        #self.list_cars[car].goto(self.xcor() - MOVE_INCREMENT, car.starting_y)

    def speed_up_cars(self):
        self.car_speed += MOVE_INCREMENT


