import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('arquivos_de_exercicios/amongus.mp3')
pygame.mixer.music.play(loops=1, start=0.0)
input()
pygame.event.wait()
# Exercicio 21