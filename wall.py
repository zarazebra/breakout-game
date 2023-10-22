from bricks import Brick


class Wall:
    def __init__(self):
        self.x_cor = -365
        self.y_cor = 175
        self.color_pos = 0
        self.colors = ["red", "orange", "green", "yellow"]
        self.score_pts = 7
        self.bricks = []

    def building_brick_wall(self):
        for row in range(8):
            if row % 2 == 0 and row != 0:
                self.color_pos += 1
                self.score_pts -= 2
            for column in range(17):
                brick = Brick()
                brick.color(self.colors[self.color_pos])
                brick.x_pos = self.x_cor
                brick.y_pos = self.y_cor
                brick.goto(brick.x_pos, brick.y_pos)
                brick.points = self.score_pts
                self.bricks.append(brick)
                self.x_cor += 45
            self.y_cor -= 15
            self.x_cor = -365

    def wall_detect_collision(self, ball):
        for brick in self.bricks:
            if brick.detect_collision(ball):
                if brick.isvisible():
                    brick.hideturtle()
                    return brick
        return None
