import pygame

pygame.mixer.init()

pygame.init()

pygame.mixer.music.load("1.mp3")
pygame.mixer.music.play()

pygame.mixer.music.stop()
pygame.mixer.quit()
