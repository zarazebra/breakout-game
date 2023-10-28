from enum import Enum
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -50)
        self.shape("circle")
        self.color("white")
        self.ball_speed = 1
        self.speed(self.ball_speed)
        self.x_dir = 10
        self.y_dir = -10
        self.num_brick_coll = 0
        self.speed_increase = 0.5

    def move(self):
        self.goto(self.xcor() + self.x_dir, self.ycor() + self.y_dir)

    def bounce(self, type):
        if type == 'X':
            self.y_dir *= -1
        elif type == 'Y':
            self.x_dir *= -1

    def speed_up(self):
        if self.num_brick_coll % 10 == 0 and self.num_brick_coll != 0:
            self.ball_speed += self.speed_increase
            if self.ball_speed > 10:
                self.ball_speed = 10
                self.speed_increase = 0
            self.speed(self.ball_speed)

    def detect_paddle(self, paddle):
        if paddle.detect_collision(self):
            self.y_dir *= -1

    # def detect_brick(self, bricks):
    #     for brick in bricks:
    #         if brick.detect_collision(self):
    #             if brick.isvisible():
    #                 self.num_brick_coll += 1
    #                 print(self.num_brick_coll)
    #                 print(self.speedvariable)
    #                 self.speed_up()
    #                 print(self.speedvariable)
    #                 brick.hideturtle()
    #                 self.y_dir *= -1
    #                 return brick.points
    #     return 0

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