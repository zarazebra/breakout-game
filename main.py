from turtle import Screen
from paddle import Paddle
from ball import Ball

game_is_on = True

window = Screen()
window.title("Breakout Game")
window.bgcolor("black")
window.setup(800, 600)
paddle = Paddle()
ball = Ball()

window.onkey(paddle.move_right, "Right")
window.onkey(paddle.move_left, "Left")
window.listen()

while game_is_on:
    ball.moving()
    ball.detect_paddle(paddle)


window.exitonclick()

