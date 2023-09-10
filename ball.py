from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.spd=0.1


    def move(self):
        n_x=self.xcor()+self.x_move
        n_y=self.ycor()+self.y_move
        self.goto(n_x,n_y)

    def collision_y(self):
        self.y_move *= -1

    def collision_x(self):
        self.x_move *= -1
        self.spd*=0.9

