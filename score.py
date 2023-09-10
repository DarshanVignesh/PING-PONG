from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score_l = 0
        self.score_r = 0
        self.penup()
        self.hideturtle()
    def update_score(self):
        self.clear()
        self.goto(-150, 180)
        self.write(arg=self.score_l, align="center", font=('courier', 88, 'normal'))
        self.goto(150, 180)
        self.write(arg=self.score_r, align="center", font=('courier', 88, 'normal'))


    def increase_l(self):
        self.score_l+=1
        self.update_score()
    def increase_r(self):
        self.score_r+=1
        self.update_score()