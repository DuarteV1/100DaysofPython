from turtle import Screen


class SnakeScreen:
    def __init__(self):
        snake_screen = Screen()
        snake_screen.setup(width=600, height=600)
        snake_screen.bgcolor("black")
        snake_screen.title("My Snake Game")
        snake_screen.tracer(0)

