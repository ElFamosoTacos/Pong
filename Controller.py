import pygame as pg
import random

class Controller():
    def __init__(self, model):
        self.model = model
        self.tick = 0


    # Function called when there is a keyboard input to move rackets
    def processData(self, data):
        if data[pg.K_UP]:
            self.model.racket2.y -= 1
            if self.model.racket2.y <= 0:
                self.model.racket2.y += 1
        if data[pg.K_DOWN]:
            self.model.racket2.y += 1
            if self.model.racket2.y  + self.model.racket2.height>= 400:
                self.model.racket2.y -= 1
        if data[pg.K_z]:
            self.model.racket1.y -= 1
            if self.model.racket1.y <= 0:
                self.model.racket1.y += 1
        if data[pg.K_s]:
            self.model.racket1.y += 1
            if self.model.racket1.y  + self.model.racket1.height>= 400:
                self.model.racket1.y -= 1


    # Update the ball position
    # And check if it collide with upper or bottom screen
    def moveBall(self):
        self.model.ball.x += self.model.ball.direction
        self.model.ball.y += self.model.ball.directiony

        if self.model.ball.y + self.model.ball.height>= 400:
            self.model.ball.y = self.model.ball.y -1
            self.model.ball.directiony = -0.40
        elif self.model.ball.y <= 0:
            self.model.ball.y = self.model.ball.y + 1
            self.model.ball.directiony = 0.40


    # Check collision between the ball and both rackets
    def checkCollision(self):
        bottomRightCoord = (self.model.ball.x + self.model.ball.width, self.model.ball.y + self.model.ball.height)

        if self.model.ball.x <= self.model.racket1.x + self.model.racket1.width and self.model.ball.x >= self.model.racket1.x:
            if self.model.ball.y <= self.model.racket1.y + self.model.racket1.height and self.model.ball.y >= self.model.racket1.y:
                self.model.ball.direction = 1
                self.model.ball.directiony = random.randint(1, 10)/10

        if self.model.ball.x + self.model.ball.width <= self.model.racket2.x + self.model.racket2.width and self.model.ball.x + self.model.ball.width >= self.model.racket2.x:
            if self.model.ball.y <= self.model.racket2.y + self.model.racket2.height and self.model.ball.y >= self.model.racket2.y:
                self.model.ball.direction = -1
                self.model.ball.directiony = -random.randint(1, 10)/10

        if self.model.ball.x <= self.model.racket1.x + self.model.racket1.width and self.model.ball.x >= self.model.racket1.x:
            if bottomRightCoord[1] <= self.model.racket1.y + self.model.racket1.height and bottomRightCoord[1] >= self.model.racket1.y:
                self.model.ball.direction = 1
                self.model.ball.directiony = random.randint(1, 10) / 10

        if self.model.ball.x + self.model.ball.width <= self.model.racket2.x + self.model.racket2.width and self.model.ball.x + self.model.ball.width >= self.model.racket2.x:
            if bottomRightCoord[1] <= self.model.racket2.y + self.model.racket2.height and bottomRightCoord[1] >= self.model.racket2.y:
                self.model.ball.direction = -1
                self.model.ball.directiony = -random.randint(1, 10)/10


    # Check if the ball get past the right or left screen
    def checkGoal(self):
        if self.model.ball.x <= 0:
            self.model.ball.x = 400
            self.model.ball.y = 200
            self.model.score2 += 1
        elif self.model.ball.x >= 800:
            self.model.ball.x = 400
            self.model.ball.y = 200
            self.model.score1 += 1



    def update(self):
        self.tick += 1

        if self.tick == 3:
            self.checkCollision()
            self.checkGoal()
            self.moveBall()
            self.tick = 0