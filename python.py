import pygame


size = 500


def draw_window(surface):
    surface.fill((0, 0, 0))
    pygame.display.update()


def main():
    window = pygame.display.set_mode((size, size))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.update()

        pygame.time.delay(50)
        pygame.time.Clock().tick(60)

        draw_window(window)


main()
