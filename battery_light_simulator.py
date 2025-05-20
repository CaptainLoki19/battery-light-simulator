import pygame 

import sys 

import time 

 

pygame.init() 

 

# Screen setup 

WIDTH, HEIGHT = 600, 400 

screen = pygame.display.set_mode((WIDTH, HEIGHT)) 

pygame.display.set_caption("Battery Light Simulator") 

 

# Font setup 

font = pygame.font.SysFont(None, 48) 

 

# Variables 

battery = 0  # start at 0% 

light_on = False 

last_update = time.time() 

 

clock = pygame.time.Clock() 

 

running = True 

while running: 

    keys = pygame.key.get_pressed() 

    current_time = time.time() 

 

    for event in pygame.event.get(): 

        if event.type == pygame.QUIT: 

            running = False 

 

    # Update battery once per second 

    if current_time - last_update >= 1: 

        if keys[pygame.K_SPACE] and battery < 100: 

            battery += 1 

        elif not keys[pygame.K_SPACE] and battery > 0: 

            battery -= 1 

        last_update = current_time 

 

    # Determine light state 

    if battery > 0: 

        light_on = True 

    else: 

        light_on = False 

 

    # Draw screen 

    if light_on: 

        screen.fill((255, 255, 255))  # White background 

        light_text = font.render("Light: On", True, (0, 0, 0)) 

    else: 

        screen.fill((0, 0, 0))  # Black background 

        light_text = font.render("Light: Off", True, (255, 255, 255)) 

 

    battery_text = font.render(f"Battery: {battery}%", True, (255, 0, 0) if battery <= 10 else (0, 0, 255)) 

 

    screen.blit(light_text, (WIDTH // 2 - light_text.get_width() // 2, HEIGHT // 3)) 

    screen.blit(battery_text, (WIDTH // 2 - battery_text.get_width() // 2, HEIGHT // 2)) 

 

    pygame.display.flip() 

    clock.tick(60) 

 

pygame.quit() 

sys.exit() 