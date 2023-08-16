from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from wall import Wall
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

wall_up = Wall((0, 290))
wall_down = Wall((0, -280))

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=paddle_r.move_paddle_up, key="Up")
screen.onkey(fun=paddle_r.move_paddle_down, key="Down")
screen.onkey(fun=paddle_l.move_paddle_up, key="w")
screen.onkey(fun=paddle_l.move_paddle_down, key="s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_the_ball()

    # detect collision with wall
    if ball.ycor() > 275 or ball.ycor() < - 266:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_score_l()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_score_r()

screen.exitonclick()
