from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def reset(self):
        super().reset()
        self.__init__()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())
