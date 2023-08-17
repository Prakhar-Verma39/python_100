from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-210, 270)
        self.color("black")
        self.write(f"LEVEL {self.level}", False, align="center", font=('Arial', 16, 'bold'))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.goto(-210, 270)
        self.color("black")
        self.write(f"LEVEL {self.level}", False, align="center", font=('Arial', 16, 'bold'))

    def finish_game(self):
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", False, align="center", font=('Arial', 24, 'bold'))