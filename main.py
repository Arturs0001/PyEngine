import pygame
import time

pygame.init()
screen = pygame.display.set_mode((640, 580))
clock = pygame.time.Clock()
fps = 60
build = 'v1.0.4'

icon = pygame.image.load("images/logo.png")
github_icon = pygame.image.load('images/github_logo.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("PyEngine")

font = pygame.font.SysFont("Arial", 28)

WHITE = (255, 255, 255)
LIGHT_GRAY = (150, 150, 150)
DARK_GRAY = (50, 50, 50)
BG_COLOR = (39, 49, 46)
GREEN = (39, 49, 46)

left_panel = pygame.Rect(0, 0, 216, 580)
right_panel = pygame.Rect(216, 0, 504, 580)


class Button:
    def __init__(self, rect, text, callback):
        self.rect = rect
        self.text = text
        self.callback = callback
        self.hovered = False

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        self.hovered = self.rect.collidepoint(mouse_pos)
        color = DARK_GRAY if self.hovered else GREEN
        pygame.draw.rect(screen, color, self.rect)

        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered and event.button == 1:
                self.callback()

def create_project():
    print("Creating project")
    time.sleep(0.1)

def open_project():
    print("Opening project")
    time.sleep(0.1)

def settings():
    print("Settings opened")
    time.sleep(0.1)

def github():
    print('Github opened')
    time.sleep(0.1)

def discord():
    print('Discord opened')
    time.sleep(0.1)

buttons = [
    Button(pygame.Rect(250, 150, 220, 60), "Create Project", create_project),
    Button(pygame.Rect(250, 230, 220, 60), "Open Project", open_project),
    Button(pygame.Rect(250, 310, 48, 48), "", github),
    Button(pygame.Rect(330, 310, 48, 48), "", discord),
]

settings_button = Button(pygame.Rect(10, 520, 48, 48), "", settings)

running = True
while running:
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, DARK_GRAY, left_panel)
    pygame.draw.rect(screen, LIGHT_GRAY, right_panel)


    for button in buttons:
        button.draw(screen)
    settings_button.draw(screen)
    screen.blit(pygame.transform.scale(icon, (48, 48)), (10, 520))
    screen.blit(pygame.transform.scale(github_icon, (48, 48)), (250, 310))
    pygame.display.set_caption(f"PyEngine | FPS: {int(clock.get_fps())} | Build: {(build)}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in buttons + [settings_button]:
            button.handle_event(event)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
