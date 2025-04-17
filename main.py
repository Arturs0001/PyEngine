import time
import pygame

pygame.init()
screen = pygame.display.set_mode((720, 640))
fps = 60
clock = pygame.time.Clock()
icon = pygame.image.load("logo.png")  
pygame.display.set_icon(icon)
font = pygame.font.SysFont("Arial", 24)

WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
DARKGRAY = (60, 60, 60)
LIGHTGRAY = (200, 200, 200)
GREEN = (0, 200, 0)

screen_width, screen_height = screen.get_size()
left_panel_width = int(screen_width * 0.3)
right_panel_width = screen_width - left_panel_width
bottom_panel_height = int(screen_height * 0.1)

def draw_button(screen, rect, text, callback=None):
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    color = GREEN
    if rect.collidepoint(mouse_pos):
        color = GRAY
        if mouse_click[0]:
            color = DARKGRAY
            if callback:
                callback()

    pygame.draw.rect(screen, color, rect)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def create_project():
    print("Create Project...")
    time.sleep(0.1)

def open_project():
    print("Open Project...")
    time.sleep(0.1)

def open_settings():
    print("Open Settings...")
    time.sleep(0.1)

running = True

create_btn_rect = pygame.Rect(left_panel_width + 40, 200, 200, 50)
open_btn_rect = pygame.Rect(left_panel_width + 40, 270, 200, 50)

settings_btn_rect = pygame.Rect(10, screen_height - bottom_panel_height + 10, 40, 40)

while running:
    screen.fill(LIGHTGRAY)

    left_panel = pygame.Rect(0, 0, left_panel_width, screen_height - bottom_panel_height)
    pygame.draw.rect(screen, DARKGRAY, left_panel)

    right_panel = pygame.Rect(left_panel_width, 0, right_panel_width, screen_height - bottom_panel_height)
    pygame.draw.rect(screen, GRAY, right_panel)

    bottom_panel = pygame.Rect(0, screen_height - bottom_panel_height, screen_width, bottom_panel_height)
    pygame.draw.rect(screen, DARKGRAY, bottom_panel)

    draw_button(screen, create_btn_rect, "Create Project", create_project)
    draw_button(screen, open_btn_rect, "Open Project", open_project)

    draw_button(screen, settings_btn_rect, "⚙", open_settings)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.set_caption(f"PyEngine | FPS: {int(clock.get_fps())}")
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
