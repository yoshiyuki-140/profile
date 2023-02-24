# coding:utf-8

import pygame
from pygame.locals import *

if __name__ == '__main__':

    WINDOW = pygame.Rect(0, 0, 500, 300)
    Ball = pygame.Rect(0, 0, 10, 10)    # Ball object's height and width have to same value.
    speed = [1, 2]
    FPS = 60

    pygame.init()
    pygame.display.set_mode(WINDOW.size)
    pygame.display.set_caption("the falling ball")

    screen = pygame.display.get_surface()

    clock = pygame.time.Clock()

    # func for collision handling
    def collide_handlings(circle_center: tuple, circle_radius: int, WINDOW: pygame.Rect):
        global speed
        # judge side collision
        if circle_center[0] - circle_radius < 0 or \
                WINDOW.width < circle_center[0] + circle_radius:
            speed[0] = -speed[0]
        # judge uppper and lower side collision
        if (circle_center[1] - circle_radius) < 0 or \
                (circle_center[1] + circle_radius) > WINDOW.bottom:
            speed[1] = -speed[1]


    # main loop
    running = True
    while running:
        clock.tick(FPS)

        # update object's vector of speed
        collide_handlings(Ball.center, Ball.height//2, WINDOW)
        Ball.move_ip(speed)

        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), Ball.center, Ball.height//2)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        pygame.display.flip()

    quit()
