import pygame

W = 800
H = 600
WHITE = (255, 255, 255)
YELLOW = (255, 250, 0)
BLUE = (0, 0, 64)

pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('TEXT')
screen.fill(BLUE)

surf = pygame.Surface((50, 50))
surf.fill((200, 0, 10))
screen.blit(surf, (375,170))

font = pygame.font.SysFont('Arial', 61, True, False)
font2 = pygame.font.SysFont('Arial', 31, True, False)

screen.blit(font.render("Всем привет", True, WHITE), (220, 230))
screen.blit(font2.render("задание на урок", True, YELLOW), (270, 300))


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
               run = False


    pygame.display.update()

