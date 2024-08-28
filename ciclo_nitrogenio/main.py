import pygame
from pygame.math import Vector2 as Vector

SCREEN_SIZE = (800,600)

COLORS = {
    'marrom_claro': '#a95e13',
    'marrom': '#964b00',
    'marrom_escuro': '#6c3c0c',
    'azul': '#69b4ff',
    'verde': '#a2ba70',
    'preto': '#000000',
    'branco': '#ffffff'     
}

STAGES = [
    {"id": 1, "to": [2], "name": "Fixação", "color": COLORS['azul'], "pos": (200, 300), "info": "Conversão de N2 atmosférico em formas utilizáveis"},
    {"id": 2, "to": [3], "name": "Nitrificação", "color": COLORS['verde'], "pos": (400, 150), "info": "Conversão de amônia em nitrato"},
    {"id": 3, "to": [4], "name": "Assimilação", "color": COLORS['marrom'], "pos": (600, 300), "info": "Absorção de nitrogênio por organismos"},
    {"id": 4, "to": [1], "name": "Desnitrificação", "color": COLORS['marrom_claro'], "pos": (400, 450), "info": "Conversão de nitrato em N2 gasoso"}
]

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.selected_stage = None
        pygame.display.set_caption('Simulador')
        self.load_assets()
    
    def load_assets(self):
        self.font = pygame.font.Font(None, 40)

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
        pygame.quit()
        exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.selected_stage = None
                for stage in STAGES:
                    if Vector(stage['pos']).distance_to(Vector(event.pos)) <= 50:
                        self.selected_stage = stage
                        break
        return True

    def get_stage(self, stage_id):
        return [stage for stage in STAGES if stage['id'] == stage_id][0]

    def draw_cycle(self):
        for stage in STAGES:
            pygame.draw.circle(self.screen, stage["color"], stage["pos"], 50)
            text = self.font.render(stage["name"], True, COLORS['preto'])
            text_rect = text.get_rect(center=(stage["pos"][0], stage["pos"][1] + 70))
            self.screen.blit(text, text_rect)
        
        for stage in STAGES:
            for target_id in stage['to']:
                self.draw_arrow(stage['pos'], self.get_stage(target_id)['pos'])
        
        if self.selected_stage:
            info_text = self.font.render(self.selected_stage["info"], True, COLORS['preto'], COLORS['branco'])
            info_rect = info_text.get_rect(center = (400,40))
            self.screen.blit(info_text, info_rect)

    def draw_arrow(self, start, end):
            v0, v1 = Vector(start), Vector(end)
            diff = (v1-v0)
            length = diff.length()
            v2 = (diff.normalize()*(length-20))+v0
            offset = diff.normalize().rotate(90)
            
            pygame.draw.line(self.screen, COLORS['preto'], start, end, 2)
            pygame.draw.polygon(
                self.screen,
                COLORS['preto'],
                [end,v2+offset*10,v2+offset*-10]
            )

    def update(self):
        self.screen.fill("#03a5fc")
        self.draw_cycle()
        pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()

