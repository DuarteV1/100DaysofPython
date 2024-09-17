from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "left"
STARTING_POSITION = (-290, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # Create a writing turtle
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(STARTING_POSITION)
        self.write(arg=f"Level: {self.score}", align=ALIGN, font=FONT)

    def level_up(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Level: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="CENTER", font=FONT)
