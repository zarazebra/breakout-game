from turtle import Turtle


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=2)
        self.xpos = -350
        self.ypos = 200
        self.brickcolor = ["red", "orange", "green", "yellow"]

    def creating_brickwall(self):
        for row in range(7):
            if row % 2 == 0:
                self.color("orange")
            for brick in range(10):
                self.goto(self.xpos, self.ypos)
                self.xpos += 10
            self.ypos -= 10




