from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0,220)
        self.points = 0
        self.max_points = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.points}/{self.max_points}")

    def add_point(self):
        self.clear()
        self.points += 1
        self.update()