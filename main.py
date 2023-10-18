from turtle import Screen
from paddle import Paddle

window = Screen()
window.title("Breakout Game")
window.bgcolor("black")
window.setup(800, 600)


paddle = Paddle()
window.onkey(paddle.move_right, "Right")
window.onkey(paddle.move_left, "Left")
window.listen()

window.exitonclick()
window.mainloop()
