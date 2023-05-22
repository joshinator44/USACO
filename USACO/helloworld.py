import random
import time
import turtle

delay = 0.1

score = 0
high_score = 0

#setup screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("yellow")
wn.setup(height=600, width=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.penup()
head.speed(0)
head.goto(0, 0)
head.direction = "stop"

#snake good
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

#scoreboard
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Score: 0 High Score: 0", align="center", font=("ds-digital", 24, "normal"))

#functions
def go_up():
    if direction != "down":
        direction = "up"
def go_down():
    if direction != "up":
        direction = "down"
def go_left():
    if direction != "right":
        direction = "left"
def go_right():
    if direction != "left":
        direction = "right"

