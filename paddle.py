from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(0, -270)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")

