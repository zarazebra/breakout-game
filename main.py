from turtle import Screen

from game import Game

window = Screen()
window.title("Breakout Game")
window.bgcolor("black")
window.setup(800, 600)


game = Game(window)
window.update()
game.start()
window.exitonclick()
