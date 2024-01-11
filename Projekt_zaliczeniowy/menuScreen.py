import pygame
import repository

pygame.init()

class Menu():
    def __init__(self):
        pass
    
    def draw(self, screen):
        screen.blit(repository.MenuTitle, (90,30))
        repository.TopsisBtn.draw(screen)
        repository.RSMBtn.draw(screen)
        repository.SPBtn.draw(screen)
        repository.UTEBtn.draw(screen)

        if  repository.TopsisBtn.action == True:
            repository.state = repository.ScreenState.TOPSIS
            repository.TopsisBtn.action = False

        if  repository.RSMBtn.action == True:
            repository.state = repository.ScreenState.RSM
            repository.RSMBtn.action = False

        if  repository.SPBtn.action == True:
            repository.state = repository.ScreenState.SP
            repository.SPBtn.action = False

        if repository.UTEBtn.action == True:
            repository.state = repository.ScreenState.UTE
            repository.UTEBtn.action = False