import pygame


class Engine:
    def __init__(self):
        screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
        screen.fill((0, 0, 0))