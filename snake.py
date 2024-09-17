import turtle
from turtle import Turtle, Screen
# The reason to put our constants here is for simplicity's sake. If we want to change them, we don't have to
# search all the code. It right here, on the top
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
turtle.mode("standard")
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
screen = Screen()


class Snake:
    def __init__(self, forma):
        self.shape = forma
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(self.shape)
        new_segment.color("pink")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Append new segment to the snake
        self.add_segment(self.segments[-1].position())

    # if we just use for segment in segments: seg.forward(20) we have a problem
    # when we tell the first segment to turn right, the rest of the body will continue to move forward
    # We need to make sure that the 2nd segment goes to the place where the first segment was,
    # and that the same happens to the other pieces.

    def move(self):
        # seg_num in range(start=2, stop=0, step=-1)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # new_x = segments[seg_num - 1].xcor()
            # new_y = segments[seg_num - 1].ycor()
            position = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(position[0], position[1])
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            for _ in range(len(self.segments)):
                self.segments[_].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            for _ in range(len(self.segments)):
                self.segments[_].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            for _ in range(len(self.segments)):
                self.segments[_].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            for _ in range(len(self.segments)):
                self.segments[_].setheading(RIGHT)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]