from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.speed(0)
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=('Arial', 24, 'normal'))

    def game_over(self):
        self.penup()
        self.home()
        self.write("Game Over.", align="center", font=("Arial", 24, 'bold'))
