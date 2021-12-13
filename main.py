import time

import pygame
from tkinter import *
import actions

root = Tk()
height = root.winfo_screenheight()
width = root.winfo_screenwidth()

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
running = True
while running:
    events = pygame.event.get()
    if bool(events):
        events = [events[0]]
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            actions.jump(width, height, screen)
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, height - height // 4), (width, height - height // 4), 1)  # floor
    pygame.draw.rect(screen, (255, 255, 255), (width // 3, height - height // 4 - 69, 70, 70), 1)  # cube
    pygame.display.flip()
pygame.quit()
