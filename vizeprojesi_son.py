import pygame

pygame.init()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Vize Projesi")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#nokta koordinatları
dot_i    = [(40,230),(40,270),(80,270),(80,230),(40,230)]
letter_i = [(40,300),(40,500),(80,500),(80,300),(40,300)]
letter_l = [(180,300),(180,500),(370,500),(370,455),(225,455),(225,300),(180,300)]
letter_k = [(435,300),(435,500),(480,500),(480,400),(600,500),(660,500),(525,390),(650,300),(590,300),(480,380),(480,300),(435,300)]
letter_e = [(730,300),(730,500),(930,500),(930,455),(775,455),(775,400),(865,400),(865,375),(775,375),(775,335),(930,335),(930,300),(730,300)]
letter_r = [(1015,300),(1015,500),(1060,500),(1060,420),(1100,420),(1180,500),(1240,500),(1150,420),(1215,420),(1215,300),(1015,300)]
hole_r   = [(1060,335),(1060,390),(1175,390),(1175,335),(1060,335)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    #çizim
    pygame.draw.lines(screen, BLACK, False, dot_i,    3)
    pygame.draw.lines(screen, BLACK, False, letter_i, 3)
    pygame.draw.lines(screen, BLACK, False, letter_l, 3)
    pygame.draw.lines(screen, BLACK, False, letter_k, 3)
    pygame.draw.lines(screen, BLACK, False, letter_e, 3)
    pygame.draw.lines(screen, BLACK, False, letter_r, 3)
    pygame.draw.lines(screen, BLACK, False, hole_r,   3)

    pygame.display.flip()

pygame.quit()
