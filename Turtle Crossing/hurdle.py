from turtle import Turtle
import random


class Hurdle(Turtle):

    def __init__(self):
        super().__init__()
        self.speed = 10
        self.design_hurdle()

    def design_hurdle(self):
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        self.color(r, g, b)
        self.goto(random.randint(250, 500), random.randint(-250, 250))
        self.setheading(180)

    def reset(self):
        super().reset()
        self.design_hurdle()

    def move_the_hurdle(self):
        if self.xcor() < -300:
            self.reset()
        self.forward(self.speed)

    def speed_increment(self):
        self.speed += 5
