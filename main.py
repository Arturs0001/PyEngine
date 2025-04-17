import pygame
import time

pygame.init()
screen = pygame.display.set_mode((720, 640))
clock = pygame.time.Clock()
fps = 60

icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("PyEngine")

font = pygame.font.SysFont("Arial", 28)

WHITE = (255, 255, 255)
LIGHT_GRAY = (180, 180, 180)
DARK_GRAY = (50, 50, 50)
BG_COLOR = (30, 30, 30)
GREEN = (0, 200, 0)

left_panel = pygame.Rect(0, 0, 216, 576)
right_panel = pygame.Rect(216, 0, 504, 576)
bottom_panel = pygame.Rect(0, 576, 720, 64)

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
    print("Creating project...")
    time.sleep(0.1)

def open_project():
    print("Opening project...")
    time.sleep(0.1)

def settings():
    print("Settings opened.")
    time.sleep(0.1)

buttons = [
    Button(pygame.Rect(250, 150, 220, 60), "Create Project", create_project),
    Button(pygame.Rect(250, 230, 220, 60), "Open Project", open_project),
]

settings_button = Button(pygame.Rect(10, 586, 48, 48), "", settings)

running = True
while running:
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, DARK_GRAY, left_panel)
    pygame.draw.rect(screen, LIGHT_GRAY, right_panel)
    pygame.draw.rect(screen, DARK_GRAY, bottom_panel)

    # Draw buttons
    for button in buttons:
        button.draw(screen)
    settings_button.draw(screen)
    screen.blit(pygame.transform.scale(icon, (48, 48)), (10, 586))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in buttons + [settings_button]:
            button.handle_event(event)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
