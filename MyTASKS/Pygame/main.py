import os
from platform import python_branch
import pygame

WIDTH, HEIGHT = 900,500

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game!!")

WHITE = (255,255,255)
SPACESHIP_WIDHT,SPACESHIP_HEIGHT = 55,40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Pygame","Assets","spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDHT,SPACESHIP_HEIGHT)),90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Pygame", "Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDHT,SPACESHIP_HEIGHT)),270)

def draw_window(red,yellow):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    pygame.display.update()

FPS = 60

def main():
    red = pygame.Rect(100,300,SPACESHIP_WIDHT,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(700,300,SPACESHIP_WIDHT,SPACESHIP_HEIGHT)
    
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        red.y += 1
        draw_window(red,yellow)

    pygame.quit()

if __name__ == "__main__":
    main()
