from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 250)
        self.score_l = 0
        self.score_r = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score_l}   {self.score_r}", align=ALIGNMENT, font=FONT)

    def increase_score_l(self):
        self.score_l += 1
        self.update_score()

    def increase_score_r(self):
        self.score_r += 1
        self.update_score()
