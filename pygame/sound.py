#!/usr/bin/python2

import pygame
from pygame.locals import *
pygame.init()
file = '1.mp3'
soundobj = pygame.mixer.music.load(file)
pygame.mixer.music.play(-1,0.0)
import time

time.sleep(4)
pygame.mixer.music.stop()

pygame.quit()
sys.exit()

