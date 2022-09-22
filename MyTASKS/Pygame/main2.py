import os
import pygame

WIN = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Green World")
GREEN = (0,255,0)
SHIP_WIDTH, SHIP_HEIGHT = 55,40

SPACESHIP_YELLOW_IMAGE = pygame.image.load(os.path.join("Pygame","Assets","spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_YELLOW_IMAGE,(SHIP_WIDTH,SHIP_HEIGHT)),90)

SPACESHIP_RED_IMAGE = pygame.image.load(os.path.join("Pygame","Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_RED_IMAGE,(SHIP_WIDTH,SHIP_HEIGHT)),270)

def draw_window(red,yellow):
    WIN.fill(GREEN)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    pygame.display.update()

FPS = 60

def main():
    red = pygame.Rect(200,350, SHIP_WIDTH,SHIP_HEIGHT)    
    yellow = pygame.Rect(700,350,SHIP_WIDTH,SHIP_HEIGHT)

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(red,yellow)
        red.x += 1
        yellow.y += 1
    pygame.quit()

if __name__ =="__main__":
    main()
