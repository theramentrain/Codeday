import pygame
def playsound(filename):
    pygame.mixer.init()

    pygame.init()

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

   #pygame.mixer.music.stop()
    #pygame.mixer.quit()
