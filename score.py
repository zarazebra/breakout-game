from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.pendown()
        self.pencolor("white")
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "bold"))
