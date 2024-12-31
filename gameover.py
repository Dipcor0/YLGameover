import pygame
import os
import sys
from math import ceil


class GameOver(pygame.sprite.Sprite):
    def __init__(self, *args, screen=None):
        super().__init__(*args)
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.speed = 200
        self.game_over = load_image('gameover.png')

        self.image = self.game_over
        self.rect = self.image.get_rect()
        self.rect.x = -self.rect.width
        self.rect.y = 0

    def update(self, *args) -> None:
        if self.rect.x < 0:
            tick = self.clock.tick()
            self.rect.x += ceil(self.speed * tick / 1000)


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


def main():
    pygame.init()
    size = 600, 300
    running = True

    screen = pygame.display.set_mode(size)

    group_game_over = pygame.sprite.Group()
    GameOver(group_game_over, screen=screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('Blue')

        group_game_over.update()
        group_game_over.draw(screen)

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
