from enum import Enum
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -50)
        self.shape("circle")
        self.color("white")
        self.speed(1)
        self.x_dir = 10
        self.y_dir = -10

    def move(self):
        self.goto(self.xcor() + self.x_dir, self.ycor() + self.y_dir)

    def bounce(self, type):
        if type == 'X':
            self.y_dir *= -1
        elif type == 'Y':
            self.x_dir *= -1

    def detect_paddle(self, paddle):
        if paddle.detect_collision(self):
            self.y_dir *= -1

    def detect_brick(self, bricks):
        for brick in bricks:
            if brick.detect_collision(self):
                if brick.isvisible():
                    brick.hideturtle()
                    self.y_dir *= -1
                    return brick.points
        return 0

    def detect_walls(self):
        if -250 < self.ycor() < 283:
            if self.xcor() < -385 or self.xcor() > 379:
                self.x_dir *= -1
        elif self.ycor() >= 283:
            self.y_dir *= -1

    def detect_out(self):
        if self.ycor() == -270:
            print("Game Over")
            return True


    class BounceType(Enum):
        Horizontal = 1
        Vertical = 2