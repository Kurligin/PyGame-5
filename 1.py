import os
import pygame


size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)


def load_image(name, color_key=None):
    path = os.path.join('data', name)
    if not os.path.isfile(path):
        raise ValueError(f'File {path} not found')
    image = pygame.image.load(path)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Cursor(pygame.sprite.Sprite):
    cursor = load_image('cursor.png')

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Cursor.cursor
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        if pygame.mouse.get_focused():
            if args and args[0].type == pygame.MOUSEMOTION:
                self.rect.x, self.rect.y = args[0].pos
        else:
            self.rect.x, self.rect.y = -1000, -1000


def main():
    all_sprites = pygame.sprite.Group()

    cursor = Cursor(all_sprites, 0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                all_sprites.update(event)

        screen.fill(pygame.Color('black'))

        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
