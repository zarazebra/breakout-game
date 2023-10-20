from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick


def creating_brickwall():
    for row in range(7):
        for bricks in range(10):
            brickstone = Brick()
            brickstone.goto(brickstone.xpos, brickstone.ypos)
            brickstone.xpos += 10
        brickstone.ypos -= 10


game_is_on = True

window = Screen()
window.title("Breakout Game")
window.bgcolor("black")
window.setup(800, 600)

paddle = Paddle()
ball = Ball()
creating_brickwall()

window.onkey(paddle.move_right, "Right")
window.onkey(paddle.move_left, "Left")
window.listen()

while game_is_on:
    ball.moving()
    ball.detect_paddle(paddle)
    ball.detect_walls()
    if ball.detect_out():
        game_is_on = False

window.exitonclick()
