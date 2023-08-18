from turtle import Screen
from snake import Snake
from food import Food
from dashboard import Dashboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# turn off the screen display
screen.tracer(0)

game_is_on = True

snake_game = Snake()
food = Food()
dashboard = Dashboard()

screen.listen()
screen.onkey(fun=snake_game.move_up, key="Up")
screen.onkey(fun=snake_game.move_down, key="Down")
screen.onkey(fun=snake_game.move_right, key="Right")
screen.onkey(fun=snake_game.move_left, key="Left")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake_game.move_the_snake()

    # Detect the collision
    if snake_game.head.distance(food) < 15:
        food.refresh()
        snake_game.extend()
        dashboard.increase_score()

    # Detect collision with wall.
    if snake_game.head.xcor() > 280 or snake_game.head.ycor() > 280 or snake_game.head.xcor() < -280 \
            or snake_game.head.ycor() < -280:
        dashboard.reset()
        snake_game.reset()

    # Detect collision with tail.
    for segment in snake_game.snake[1:]:
        if snake_game.head.distance(segment) < 10:
            dashboard.reset()
            snake_game.reset()
    # If head collides with any segment in the tail:
        # trigger game_over

screen.exitonclick()
