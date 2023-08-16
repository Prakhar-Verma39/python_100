from turtle import Turtle


class Wall(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.1, stretch_len=38)
        self.setposition(position)