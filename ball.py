from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -135)
        self.shape("circle")
        self.color("white")
