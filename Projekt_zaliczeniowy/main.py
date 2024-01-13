import pygame 
import menuScreen
import topsisScreen
import rsmScreen
import spScreen
import repository
import uteScreen
import rankingScreen

pygame.init()
isRunningFlag = True

SCREEN_WIDTH = 800
SCREEN_HIGHT = 600

screen =pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
screen.blit(repository.BACKGROUND,(0,0))

menu = menuScreen.Menu()
topsis = topsisScreen.Topsis()
rsm = rsmScreen.RSM()
sp = spScreen.SP()
ute = uteScreen.UTE()
ranking = rankingScreen.Ranking()

while isRunningFlag:

    screen.fill((0,0,0))
    screen.blit(repository.BACKGROUND,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunningFlag = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                repository.text = repository.text[:-1]
            elif event.key == pygame.K_RETURN:
                repository.setparametersstate = repository.SetParametersState.PRZYCISKI
                repository.text = '0'
            else:
                repository.text += event.unicode
            

    if  repository.state == repository.ScreenState.TOPSIS:
        topsis.draw(screen)

    elif repository.state == repository.ScreenState.MENU:
        menu.draw(screen)

    elif repository.state == repository.ScreenState.RSM:
        rsm.draw(screen)
    
    elif repository.state == repository.ScreenState.SP:
        sp.draw(screen)

    elif repository.state == repository.ScreenState.UTE:
        ute.draw(screen)
        
    elif repository.state == repository.ScreenState.RANKING:
        ranking.draw(screen)

    pygame.display.flip()
