from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.right, "d")

while game_is_on:
  screen.update()
  time.sleep(0.1)

  snake.move()

  if snake.segments[0].distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()

  has_hit_wall = snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280

  has_hit_tail = False
  for seg in snake.segments[1:]:
    if snake.segments[0].distance(seg) < 10:
      has_hit_tail = True

  if has_hit_wall or has_hit_tail:
    game_is_on = False

scoreboard.game_over()

screen.exitonclick()
