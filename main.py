import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
fps = 60
clock = pygame.time.Clock()
running = True
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.set_caption(f"PyEngine | FPS: {int(clock.get_fps())}")
    screen.fill("green")





    pygame.display.flip()

    clock.tick(fps)

pygame.quit()