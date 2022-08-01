import pygame


class Cube(object):
    rows = 20

    def __init__(self, start, dirx=1, diry=0, color=(0, 255, 0)):
        self.pos = start
        self.dirx = dirx
        self.diry = diry
        self.color = color

    def move(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry

    def draw(self, surface, eyes=False):
        pass


class Snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirx = 1
        self.diry = 0

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.update()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.dirx = 1
                self.diry = 0
                self.turns[self.head.pos[:]] = [self.dirx, self.diry]

            elif keys[pygame.K_RIGHT]:
                self.dirx = -1
                self.diry = 0
                self.turns[self.head.pos[:]] = [self.dirx, self.diry]

            elif keys[pygame.K_UP]:
                self.dirx = 0
                self.diry = -1
                self.turns[self.head.pos[:]] = [self.dirx, self.diry]

            elif keys[pygame.K_DOWN]:
                self.dirx = 0
                self.diry = 1
                self.turns[self.head.pos[:]] = [self.dirx, self.diry]

        for c, a in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if c == len(self.body - 1):
                    self.turns.pop(p)
            else:
                if c.dirx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])

                elif c.dirx == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])

                elif c.diry == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)

                elif c.diry == -1 and c.pos[1] <= 0:
                    c.pos = (0, c.pos[1])

                else:
                    c.move(c.dirx, c.diry)

    def reset(self, pos):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def draw_grid(width, rows, surface):
    size_between = width // rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + size_between
        y = y + size_between
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))


def draw_window(surface):
    surface.fill((0, 0, 0))
    draw_grid(size, rows, surface)
    pygame.display.update()


def main():
    global size, rows, s
    size = 500
    rows = 20
    window = pygame.display.set_mode((size, size))

    s = Snake((0, 0, 0), (10, 10))

    run = True
    while run:
        pygame.event.poll()

        pygame.time.delay(50)
        pygame.time.Clock().tick(60)

        draw_window(window)


main()
