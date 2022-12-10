from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

INITIAL_SNAKE_SIZE = 5
screen = Screen()


screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.colormode(255)
screen.tracer(0)

snake = Snake(INITIAL_SNAKE_SIZE)
food = Food(580, 580)
scoreboard = Scoreboard(600)
screen.listen()
screen.onkey(key="d", fun=snake.turn_right)
screen.onkey(key="a", fun=snake.turn_left)
screen.onkey(key="w", fun=snake.turn_up)
screen.onkey(key="s", fun=snake.turn_down)

print(food.position())
while True:
    if snake.hitfood(food.position()):
        snake.grow()
        food.refresh()
        scoreboard.updatescoreboard()

    if snake.hitthewall() or snake.hititself():
        scoreboard.gameover()
        screen.exitonclick()

    snake.move_forward()
    screen.update()
    time.sleep(0.1)