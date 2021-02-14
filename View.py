import pygame as pg

class View():
    def __init__(self, model, controller):
        self.model = model
        self.controller = controller
        pg.init()
        self.screen = pg.display.set_mode((800, 400))


    # Function to send key to controller
    def notifController(self, data):
        self.controller.processData(data)


    def displayRackets(self):
        pg.draw.rect(self.screen, (255, 255, 255), (self.model.racket1.x, self.model.racket1.y, self.model.racket1.width, self.model.racket1.height), 2)
        pg.draw.rect(self.screen, (255, 255, 255), (self.model.racket2.x, self.model.racket2.y, self.model.racket2.width, self.model.racket2.height), 2)


    def displayBall(self):
        pg.draw.rect(self.screen, (255, 255, 255), (self.model.ball.x, self.model.ball.y, self.model.ball.width, self.model.ball.height), 2)


    def displayScore(self):
        font = pg.font.SysFont('Arial', 50)
        text = font.render(str(self.model.score1), False, (255,255,255))
        self.screen.blit(text, (280, 10))

        text = font.render(str(self.model.score2), False, (255, 255, 255))
        self.screen.blit(text, (500, 10))


    def display(self):
        exit = 0

        while not exit:
            # Background color
            self.screen.fill((0,0,0))

            self.displayRackets()
            self.displayBall()
            self.displayScore()

            pg.display.update()

            self.notifController(pg.key.get_pressed())
            self.controller.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit = 1
                    pg.quit()