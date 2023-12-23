import pygame as pg

from settings import SCREEN, FPS, BG


class Game:
    def __init__(self):
        pg.display.init()

        pg.event.set_blocked(None)
        pg.event.set_allowed(pg.KEYUP)

        self.sc = pg.display.set_mode(SCREEN, flags=pg.NOFRAME)
        self.clock = pg.time.Clock()
        self.dt = 0.016

        self.running = False

    def process_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYUP and event.key == pg.K_ESCAPE:
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.sc.fill(BG)

    def run(self):
        self.running = True

        while self.running:
            self.dt = self.clock.tick(FPS) / 1000

            self.process_events()
            self.update()
            self.draw()

            pg.display.flip()

        pg.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
