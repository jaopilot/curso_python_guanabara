import pygame
pygame.init()
pygame.mixer.music.set_volume(1.0)  # Volume máximo (1.0)
pygame.mixer.music.load(r'E:\Documents\Projetos Phyton\curso_python_guanabara\arquivos_de_exercicios\amongus.mp3')
pygame.mixer.music.play()
pygame.event.wait()
# Exercicio 21