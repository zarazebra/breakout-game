from turtle import Screen

from ball import Ball
from paddle import Paddle
from score import Score
from wall import Wall


class Game:

    def __init__(self, window: Screen):
        self.game_over = False
        self.border = -270
        self.paddle = Paddle()
        self.window = window
        self.setup_window()

        self.score = Score()
        self.ball = Ball()
        self.wall = Wall()
        self.wall.building_brick_wall()

    def setup_window(self):
        self.window.tracer(0)
        self.window.onkey(self.paddle.move_right, "Right")
        self.window.onkey(self.paddle.move_left, "Left")
        self.window.listen()

    def start(self):
        self.window.tracer(1)
        while not self.game_over:
            # move ball
            self.ball.move()
            self.check()

            # check coll
            brick = self.wall.wall_detect_collision(self.ball)
            if brick is not None:
                self.ball.bounce('X')
                # check score

            if self.paddle.detect_collision(self.ball):
                self.ball.bounce('X')

            self.detect_walls()

            pass

    def check(self):
        if self.ball.ycor() != self.border:
            return

        self.game_over = True
        self.score.game_over()

    def detect_walls(self):
        if -250 < self.ball.ycor() < 283:
            if self.ball.xcor() < -385 or self.ball.xcor() > 379:
                self.ball.bounce('Y')
        elif self.ball.ycor() >= 283:
            self.ball.bounce('X')
