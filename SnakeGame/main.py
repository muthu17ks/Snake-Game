# Importing all packages
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect Collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    screen.onkeypress(key='Up', fun=snake.up)
    screen.onkeypress(key='Down', fun=snake.down)
    screen.onkeypress(key='Left', fun=snake.left)
    screen.onkeypress(key='Right', fun=snake.right)

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()
# screen visibility
screen.exitonclick()
