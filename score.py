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

    def game_over(self):
        self.penup()
        self.goto(0, -50)
        self.pendown()
        self.pencolor("red")
        self.write(f"GAME OVER", align="center", font=("Courier", 50, "bold"))

    def score_points(self, brick_score):
        self.clear()
        self.score += brick_score
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "bold"))
