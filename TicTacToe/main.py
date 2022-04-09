import sys

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 640, 640
screen = pygame.display.set_mode((width, height))

gridImg = pygame.image.load("img/grid.png")
gridImg.convert()
gridImg = pygame.transform.scale(gridImg, (width, height))

gridRect = gridImg.get_rect()
# Colors
bgColor = (22, 189, 172)
black = (0, 0, 0)


# Game Functions
def drawGrid():
  screen.blit(gridImg, gridRect)


# Game loop
while True:
  screen.fill(bgColor)
  
  for event in pygame.event.get():
    mousePos = pygame.mouse.get_pos()
    if mousePos[0] < width // 3 and mousePos[1] < height // 3:
      # in top left
      print("in top left")
    if mousePos[0]
    
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  # Update
  
  # Draw
  drawGrid()
  
  pygame.display.flip()
  fpsClock.tick(fps)
