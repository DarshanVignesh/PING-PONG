from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def up(self):
        y = self.ycor() + 60
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - 60
        self.goto(self.xcor(), y)






