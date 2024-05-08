from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.penup()
        self.ht()

    def increment_scoreboard(self):
        self.level += 1

    def display_scoreboard(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def display_game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!', align='center',font=FONT)