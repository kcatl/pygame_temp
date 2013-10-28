__author__ = 'Administrator'
import pygame
pygame.init()

screen = pygame.display.set_mode((800 , 600))
all_colors = pygame.Surface((4096, 4096), depth = 24)
b = 0
for r in xrange(256):

    for g in xrange(256):

        print r, g ,b
        all_colors.set_at((r, g), (r, g, b))

pygame.image.save(all_colors, 'allcolor.bmp')