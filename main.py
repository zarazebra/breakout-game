from turtle import Screen
from paddle import Paddle
from ball import Ball

window = Screen()
window.title("Breakout Game")
window.bgcolor("black")
window.setup(800, 600)

ball = Ball()
paddle = Paddle()
window.onkey(paddle.move_right, "Right")
window.onkey(paddle.move_left, "Left")
window.listen()

window.exitonclick()
window.mainloop()
