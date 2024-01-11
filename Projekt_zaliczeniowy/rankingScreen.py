import pygame
import repository
import data

pygame.init()


class Ranking():
    def __init__(self):
        self.text = "Wprowadzone dane są niepoprawne"

    def draw(self,screen): 
        repository.WrocBtn.draw(screen)

        if repository.WrocBtn.action == True:
            repository.state = repository.ScreenState.MENU
            repository.WrocBtn.action = False
        
        if data.Ranking is None:
            font = pygame.font.Font(None, 50)
            text = font.render(self.text,True,(255,255,255))
            screen.blit(text,(100,200))
        