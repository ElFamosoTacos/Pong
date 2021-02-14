import Racket
import Ball

class Model():
    def __init__(self):
        self.racket1 = Racket.Racket(0, 0, 25, 150)
        self.racket2 = Racket.Racket(775, 0, 25, 150)
        self.ball = Ball.Ball(400, 200, 25, 25, -1)
        self.score1 = 0
        self.score2 = 0