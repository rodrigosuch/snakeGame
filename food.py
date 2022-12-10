from turtle import Turtle
import random


class Food(Turtle):
    canvaswidth = 0
    canvasheigth = 0

    def __init__(self, w, h):
        super().__init__()
        self.canvaswidth = w
        self.canvasheigth = h
        self.shape("circle")
        self.color("white")
        self.speed(0)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        posx = random.randint(-self.canvaswidth/2, self.canvaswidth/2)
        posy = random.randint(-self.canvasheigth/2, self.canvasheigth/2)
        self.goto(posx,posy)

    def refresh(self):
        posx = random.randint(-self.canvaswidth/2, self.canvaswidth/2)
        posy = random.randint(-self.canvasheigth/2, self.canvasheigth/2)
        self.goto(posx, posy)
