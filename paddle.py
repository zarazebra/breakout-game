from detector import Detector


class Paddle(Detector):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(0)
        self.goto(0, -270)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")

    def move_right(self):
        if self.pos() <= (325, -270):
            self.forward(10)

    def move_left(self):
        if self.pos() >= (-330, -270):
            self.back(10)
