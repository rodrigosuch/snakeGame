from turtle import Turtle


class Scoreboard():
    score = 0
    def __init__(self, height):
        scoreboard = Turtle()
        scoreboard.color("white")
        scoreboard.penup()
        scoreboard.hideturtle()
        scoreboard.setposition((0,height/2-20))
        scoreboard.write("SCOREBOARD = 0", False, align="center")
        self.scoreboard = scoreboard

    def updatescoreboard(self):
        self.score = self.score + 1
        text = f'SCOREBOARD = {self.score}'
        self.scoreboard.clear()
        self.scoreboard.write(text, False, align="center")

    def gameover(self):
        gameover = Turtle()
        gameover.color("white")
        gameover.penup()
        gameover.hideturtle()
        gameover.write("Game Over!", False, align="center")
