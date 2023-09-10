from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen=Screen()
score=Score()

screen.title("PING PONG")
screen.bgcolor("black")

screen.setup(width=800,height=600)
screen.tracer(0)
r_p=Paddle((380,0))
l_p=Paddle((-380,0))
screen.listen()

screen.onkey(l_p.up, "w")
screen.onkey(l_p.down, "s")
screen.onkey(r_p.up, "Up")
screen.onkey(r_p.down, "Down")

ball=Ball()
game=True
while game:
    time.sleep(ball.spd)
    screen.update()

    #detecting collison with wall
    if ball.ycor()>275 or ball.ycor()<-270:
        ball.collision_y()
    #detecting with paddle

    if ball.distance(r_p)<50 and ball.xcor()>350 or ball.distance(l_p)<50 and ball.xcor()<-350:
        ball.collision_x()

    score.update_score()
    if ball.xcor()>380:
        ball.goto(0,0)
        ball.spd=0.1
        score.increase_l()


    if ball.xcor()<-380:
        ball.goto(0,0)
        ball.spd = 0.1
        score.increase_r()


    ball.move()

















screen.exitonclick()