# Project 20: Snake Game Part 1
# Guillaume CC, aka TheFirewallDragon

import turtle
import time

from snake import Snake


GAME_SPEED = 5

wait_time = (11 - GAME_SPEED) / 30

# screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Unfinished Snake Game (Part 1)")
screen.bgcolor("black")
# disable automatic screen updates
screen.tracer(0)

# snake setup
snake = Snake()

# controls setup
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# since there is no proper "game over" condition yet, temporarily setting the game to end after 50 cycles
cycle = 0
while cycle < 50:
    screen.update()
    # to control the speed, wait for the set amount of time
    time.sleep(wait_time)
    snake.move()
    cycle += 1

# wait for click before closing the window
screen.exitonclick()