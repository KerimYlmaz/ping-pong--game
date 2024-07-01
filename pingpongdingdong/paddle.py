from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def right_up(self):
        coordinate = self.ycor()
        self.sety(coordinate + 20)

    def right_down(self):
        coordinate = self.ycor()
        self.sety(coordinate - 20)

    def left_down(self):
        coordinate = self.ycor()
        self.sety(coordinate - 20)

    def left_up(self):
        coordinate = self.ycor()
        self.sety(coordinate + 20)

