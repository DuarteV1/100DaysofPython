from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.x_position = x_position
        self.shape("square")
        # The standard square size is(20,20) pixels. So we put the multiplier value in wid and len to get the final
        # dimension we want: 100, 20
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.x_position, 0)

    def up(self):
        if self.ycor() < 230:
            new_y = self.ycor() + 30
            self.goto(self.x_position, new_y)

    def down(self):
            if self.ycor() > - 230:
                new_y = self.ycor() - 30
                self.goto(self.x_position, new_y)
