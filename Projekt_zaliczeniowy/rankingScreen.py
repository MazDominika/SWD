import pygame
import repository
import data
from copy import deepcopy

pygame.init()


class Ranking():
    def __init__(self):
        self.text = "Wprowadzone dane są niepoprawne"

    def draw(self,screen): 

        if data.Ranking is None:
            font = pygame.font.Font(None, 50)
            text = font.render(self.text,True,(255,255,255))
            screen.blit(text,(100,200))
            repository.WrocRankingScreenBtn.draw(screen)
        
            if repository.WrocRankingScreenBtn.action == True:
                repository.state =   repository.ScreenState .MENU
                repository.WrocRankingScreenBtn.action = False


        else:
            if repository.rankingstate == repository.RankingState.RANKING:
                screen.blit(repository.TabelaRankingu,(0,0))
                ranking = deepcopy(data.Ranking.drop('trasa', axis = 1))
                rows =ranking.index.tolist()
                columns = ranking.columns.tolist()
                repository.WyswietlTraseBtn.draw(screen)
                repository.WrocRankingScreenBtn.draw(screen)

                x = 35
                y = 87
                for c in columns[:2]:
                    for r in rows[:10]:
                        text = str(ranking.loc[r,c])
                        text_list = text.split(' ', 1)
                        font = pygame.font.Font(None, 30)

                        if len(text_list) > 1:
                            text = font.render(text_list[0],True,(0,0,0))
                            screen.blit(text,(x,y))

                            text = font.render(text_list[1],True,(0,0,0))
                            screen.blit(text,(x,y + 18))
                        else:
                            text = font.render(text_list[0],True,(0,0,0))
                            screen.blit(text,(x,y + 15))
                        y += 44.5
                    x += 150
                    y = 87

                x = 305
                y = 87
                for c in columns[2:]:
                    for r in rows[:10]:
                        text = str(ranking.loc[r,c])
                        font = pygame.font.Font(None, 30)
                        text = font.render(text,True,(0,0,0))
                        screen.blit(text,(x,y + 15))
                        y += 44.5
                    x += 62.5
                    y = 87

                if repository.WrocRankingScreenBtn.action == True:
                    repository.state =   repository.ScreenState .MENU
                    repository.WrocRankingScreenBtn.action = False

                if repository.WyswietlTraseBtn.action == True:
                    repository.rankingstate =   repository.RankingState.TRASY
                    repository.WyswietlTraseBtn.action = False


            elif repository.rankingstate == repository.RankingState.TRASY:
                repository.WrocRankingScreenBtn.draw(screen)
                screen.blit(repository.TabelaTrasa,(0,0))
                rows =data.Ranking.index.tolist()

                if repository.WrocRankingScreenBtn.action == True:
                    repository.rankingstate =   repository.rankingstate .RANKING
                    repository.WrocRankingScreenBtn.action = False

                x = 35
                y = 3
                for r in rows[:10]:
                    font = pygame.font.Font(None, 30)
                    text = str(data.Ranking.loc[r,"trasa"])
                    text_list = text.split(" ", 30)
                    if len(text_list) > 15:
                        font = pygame.font.Font(None, 22)
                        text = font.render(" ".join(text_list[0:11]).replace("- -", "-"),True,(0,0,0))
                        screen.blit(text,(x,y))
                        text = font.render(" ".join(text_list[11:20]).replace("- -", "-"),True,(0,0,0))
                        screen.blit(text,(x,y+15))
                        text = font.render(" ".join(text_list[20:]).replace("- -", "-"),True,(0,0,0))
                        screen.blit(text,(x,y+30))
                    elif len(text_list) > 10:
                        text = font.render(" ".join(text_list[0:6]).replace("- -", "-"),True,(0,0,0))
                        screen.blit(text,(x,y))
                        text = font.render(" ".join(text_list[6:]).replace("- -", "-"),True,(0,0,0))
                        screen.blit(text,(x,y+18))
                    else:
                        text = font.render(text,True,(0,0,0))
                        screen.blit(text,(x,y+15))
                    y += 52.8