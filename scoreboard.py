from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 15, 'normal')
POSITION_SCOREBOARD = 0, 280


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        with open('data.txt') as file:
            self.highest_score = int(file.read())

        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(POSITION_SCOREBOARD)
        self.pendown()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} highest score: {self.highest_score}", align=ALIGN, font=FONT)

    def scored_a_point(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score

            with open("data.txt", mode='w') as file:
                file.write(f"{self.highest_score}")

        self.score = 0
        self.update_scoreboard()


'''
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)
'''