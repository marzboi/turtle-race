from turtle import Turtle, Screen
import random
from tkinter import *
from tkinter import messagebox

screen = Screen()
screen.title("Welcome to the turtle race!")


def play():
    is_race_on = False
    screen.setup(width=500, height=400)
    user_bet = ''

    while not user_bet:
        user_bet = screen.textinput(title="Make your bet",
                                    prompt="Which turtle will win the race? Enter a color: ")

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    y = 75
    all_turtle = []

    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y)
        y -= 30
        all_turtle.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:

        for turtle in all_turtle:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    messagebox.showinfo(
                        "Game!", f"You've won! the {winning_color} turtle is the winner")
                else:
                    messagebox.showinfo("Game!", f"You've lost! the {
                        winning_color} turtle is the winner")

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)


user_playing = True

while user_playing:
    play()
    user_continue = user_bet = screen.textinput(
        title="Continue?", prompt='Please type "yes" or "no"')
    if user_continue == 'no':
        user_playing = False
        screen.bye()
    else:
        screen.clear()

screen.exitonclick()
