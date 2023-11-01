from turtle import Turtle
from database import ScoreRepository


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.score_rep = ScoreRepository()
        self.score = 0
        self.highscore = self.score_rep.get_current_highscore()
        self.update_score()

    def update_score(self):
        self.clear()
        self.penup()
        self.goto(0, 280)
        self.pendown()
        self.write(f"Highscore: {self.highscore} /// Score: {self.score}", align="center", font=("Courier", 20, "bold"))

    def score_points(self, brick_score):
        self.score += brick_score
        self.update_score()

    def check_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.update_score()
            self.score_rep.add_new_highscore(self.highscore)

    def game_over(self):
        self.check_highscore()

        self.penup()
        self.goto(0, -50)
        self.pendown()
        self.pencolor("red")
        self.write(f"GAME OVER", align="center", font=("Courier", 50, "bold"))
