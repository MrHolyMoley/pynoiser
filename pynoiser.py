import pygame

sound_file = "brown-noise.mp3"
pygame.mixer.init()
sound = pygame.mixer.Sound(sound_file)

while True:
    sound.play()
    pygame.time.wait(int(sound.get_length() * 1000))




