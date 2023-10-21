from turtle import Turtle


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=2)
        self.x_pos = None
        self.y_pos = None
        self.points = None







