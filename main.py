from turtle import Screen
from paddle import Paddle

window = Screen()
window.title("Breakout Game")
window.bgcolor("black")
window.setup(800, 600)

paddle = Paddle()

window.exitonclick()
window.mainloop()
