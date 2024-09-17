from turtle import Screen
from scoreboard import Scoreboard
import paddle
import ball
import time
# Create a screen object, with 800 by 600, with black background and a Title

pong_screen = Screen()
pong_screen.setup(width=800, height=600)
pong_screen.bgcolor("black")
pong_screen.title("The Pong Game")
pong_screen.tracer(0)

# Paddle related code
r_paddle = paddle.Paddle(360)
l_paddle = paddle.Paddle(-360)

pong_screen.listen()
pong_screen.onkeypress(key="Up", fun=r_paddle.up)
pong_screen.onkeypress(key="Down", fun=r_paddle.down)
pong_screen.onkeypress(key="w", fun=l_paddle.up)
pong_screen.onkeypress(key="s", fun=l_paddle.down)

ball = ball.Ball()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    pong_screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with Top/Bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # if it's a miss
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_scored_a_point()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_scored_a_point()

Screen().exitonclick()
