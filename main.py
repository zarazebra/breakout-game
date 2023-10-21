from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick
from score import Score

game_is_on = True
x_cor = -365
y_cor = 175
color_pos = 0
colors = ["red", "orange", "green", "yellow"]
points = 7


def building_brick_wall(x_pos, y_pos, color, score):
    for row in range(8):
        if row % 2 == 0 and row != 0:
            color += 1
            score -= 2
        for column in range(17):
            brick = Brick()
            brick.color(colors[color])
            brick.goto(x_pos, y_pos)
            brick.points = score
            x_pos += 45
        y_pos -= 15
        x_pos = -365


window = Screen()
window.tracer(0)
window.title("Breakout Game")
window.bgcolor("black")
window.setup(800, 600)

paddle = Paddle()
ball = Ball()
score = Score()

building_brick_wall(x_cor, y_cor, color_pos, points)

window.onkey(paddle.move_right, "Right")
window.onkey(paddle.move_left, "Left")
window.listen()

window.update()

while game_is_on:
    window.tracer(1)
    ball.moving()
    ball.detect_paddle(paddle)
    ball.detect_walls()
    if ball.detect_out():
        game_is_on = False

window.exitonclick()
