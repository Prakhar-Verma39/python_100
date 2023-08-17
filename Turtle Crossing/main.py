import time
from turtle import Screen
from player import Player
from hurdle import Hurdle
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.colormode(255)

screen.tracer(0)

FINISH_LINE_Y = 270
game_is_on = True
player = Player()

hurdles = []
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=player.move_right, key="Right")


def level_up():
    global FINISH_LINE_Y, game_is_on

    # randomly generate 0 - 4 more hurdles each time
    for _ in range(4 + random.randint(0, 2)):
        hurdles.append(Hurdle())

    while game_is_on:
        time.sleep(0.1)

        # moving each hurdle
        for hurdle in hurdles:
            hurdle.move_the_hurdle()

            # detect collision with hurdles
            if player.distance(hurdle) < 20:
                scoreboard.finish_game()
                game_is_on = False

        # detect if player reached to the end, to level up the speed and number of hurdles
        if player.ycor() > FINISH_LINE_Y:
            player.reset()
            scoreboard.increase_level()
            for hurdle in hurdles:
                hurdle.speed_increment()
            level_up()

        screen.update()


# first call to begin the game
level_up()

screen.exitonclick()
