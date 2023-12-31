# Project 19: Turtle Race
# Guillaume CC, aka TheFirewallDragon


import turtle
import random


FRAME_WIDTH = 600
FRAME_HEIGHT = 400
COLOR_LIST = ["red", "orange", "yellow", "green", "blue", "purple"]
SPEED = 10

# screen setup
screen = turtle.Screen()
screen.setup(width=FRAME_WIDTH, height=FRAME_HEIGHT)
screen.title("Turtle Race")

# find the location of the first racer, count an extra one so there is some offset from the edge
offset = int(FRAME_HEIGHT / (len(COLOR_LIST) + 1))
start_x = FRAME_WIDTH / -2 + 12
start_y = int(FRAME_HEIGHT / -2 + offset)

# initialize all turtles, based on the number of colors
racers = len(COLOR_LIST)
racer_list = []
for i in range(racers):
    racer_list.append(turtle.Turtle(shape="turtle"))
    racer_list[i].hideturtle()
    racer_list[i].color(COLOR_LIST[i])
    racer_list[i].penup()
    racer_list[i].setx(start_x)
    racer_list[i].sety(start_y + offset * i)
    racer_list[i].showturtle()

# ask for input, for simplicity, accept whatever is entered
guess = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color:")

# the finish line, offset from the right edge
end_x = FRAME_WIDTH / 2 - 25
race_is_over = False
winner = ""
# the race loop
while not race_is_over:
    for i in range(racers):
        racer_list[i].setx(racer_list[i].xcor() + random.randint(1, SPEED))
        if racer_list[i].xcor() >= end_x:
            race_is_over = True
            winner = COLOR_LIST[i]

print(f"The winner was {winner}.")
if guess.lower() == winner.lower():
    print("You won the bet!")
else:
    print("Sorry, you lost.")

screen.exitonclick()