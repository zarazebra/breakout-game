from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from wall import Wall

game_is_on = True

window = Screen()
window.tracer(0)
window.title("Breakout Game")
window.bgcolor("black")
window.setup(800, 600)

paddle = Paddle()
ball = Ball()
score = Score()
wall = Wall()

wall.building_brick_wall()

window.onkey(paddle.move_right, "Right")
window.onkey(paddle.move_left, "Left")
window.listen()

window.update()

while game_is_on:
    window.tracer(1)
    ball.moving()
    ball.detect_paddle(paddle)
    score_point = ball.detect_brick(wall.bricks)
    ball.detect_walls()
    score.score_points(score_point)
    if ball.detect_out():
        game_is_on = False
        score.game_over()

window.exitonclick()
