from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


def register_event_listeners():
    screen.onkeypress(move_forwards, 'w')
    screen.onkeypress(move_backwards, 's')
    screen.onkeypress(turn_right, 'd')
    screen.onkeypress(turn_left, 'a')
    screen.onkeypress(clear, 'c')


register_event_listeners()


screen.listen()
screen.exitonclick()
