from turtle import Turtle

from ball import Ball


class Detector(Turtle):
    def __init__(self):
        super().__init__()
        self.length = self.shapesize()[1]
        self.width = self.shapesize()[0]
        self.default_size = 10

    def detect_collision(self, ball: Ball):
        diff_x = abs(self.xcor() - ball.xcor())
        diff_y = abs(self.ycor() - ball.ycor())
        diff_width = ((self.shapesize()[0] + ball.shapesize()[0]) / 2) * self.default_size
        diff_length = ((self.shapesize()[1] + ball.shapesize()[1]) / 2) * self.default_size

        collision = diff_x <= diff_length and diff_y <= diff_width

        return collision

