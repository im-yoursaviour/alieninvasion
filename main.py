import sys, pygame
from settings import Settings


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """ Initialize game and create game resources"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(size=(self.settings.screen_width, self.settings.screenHeight))
        pygame.display.set_caption("Alien invasion")


    def run_game(self):
        """ Start the main loop for the game"""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            # make the most recently drawn screen visible .
            pygame.display.flip()



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

