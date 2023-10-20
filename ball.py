from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -100)
        self.shape("circle")
        self.color("white")
        self.speed(1)
        self.x_dir = 10
        self.y_dir = -10

    def moving(self):
        self.goto(self.xcor() + self.x_dir, self.ycor() + self.y_dir)

    def detect_paddle(self, paddle):
        if self.ycor() <= -250:
            if paddle.xcor() - 50 <= self.xcor() <= paddle.xcor() + 50:
                self.x_dir *= -1
                self.y_dir *= -1

