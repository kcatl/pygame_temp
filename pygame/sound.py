#!/usr/bin/python2

import pygame
from pygame.locals import *
pygame.init()
file = '1.mp3'
soundobj = pygame.mixer.music.load(file)
soundobj.mixer.music.play(-1,0.0)
import time

time.sleep(4)
soundobj.stop()

pygame.quit()
