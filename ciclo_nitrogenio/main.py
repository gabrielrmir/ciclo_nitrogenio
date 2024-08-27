import pygame

SCREEN_SIZE = (400,300)

COLORS = {
    'marrom_claro': '#a95e13',
    'marrom': '#964b00',
    'marrom_escuro': '#6c3c0c',
    'azul': '#69b4ff',
    'verde': '#a2ba70'
}

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Simulador')

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.update()
            self.draw()
    
    def update(self):
        pass

    def draw(self):
        self.screen.fill("#03a5fc")
        pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()

