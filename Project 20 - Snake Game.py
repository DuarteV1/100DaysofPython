from scoreboard import ScoreBoard
from screen import SnakeScreen
from turtle import Screen
from snake import Snake
from food import Food
import time
# Create a screen object, with 600 by 600, with black background and a Tile

snake_screen = SnakeScreen()
screen = Screen()
forma = screen.textinput("Shape", "Choose a shape: 'arrow', 'circle', 'classic', 'square', 'triangle', 'turtle':")

scoreboard = ScoreBoard()

# Create a snake object from Snake class, on a separated file
snake = Snake(forma)
food = Food(forma)
screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# Move the snake on the screen automatically forward
game_is_on = True
while game_is_on:
    screen.update()
    # se usar 0.046 o tempo de atualização do ecrã é rápido o suficiente para não dar erro
    time.sleep(0.1)
    # When the program is sleeping, it is still able to take actions from the move module.
    # which means that if i press up and left, the turtle head turn up, then left, and then move. meaning
    # that it didn't move when it was turning up
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.scored_a_point()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()


screen.exitonclick()
