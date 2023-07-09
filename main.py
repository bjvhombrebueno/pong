from turtle import Screen, Turtle
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid =5, stretch_len=1 )
paddle.penup()
paddle.speed("fastest")
paddle.goto(350,0)

def go_up():
    while paddle.ycor() < 250:
        paddle.sety(paddle.ycor() + 20)


def go_down():
    while paddle.ycor() > -250:
        paddle.sety(paddle.ycor() - 20)

screen.listen()
screen.onkeypress(go_up,"Up")
screen.onkeypress(go_down,"Down")

game_is_on = True
while game_is_on:
    screen.update()
    #time.sleep(0.1)


screen.exitonclick()

