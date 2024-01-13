import pygame
from enum import Enum

class ScreenState(Enum):
    MENU = 1
    TOPSIS = 2
    RSM = 3
    SP = 4
    UTE = 5
    RANKING = 6

class SetParametersState(Enum):
    WYSOKOSC = 1
    DLUGOSC = 2
    PRZEWYZSZENIA = 3
    CZAS = 4
    TEMP_LATO = 5
    TEMP_ZIMA = 6
    GOT = 7
    OCENA_GOOGLE = 8
    PRZYCISKI = 9
    
setparametersstate = SetParametersState.PRZYCISKI
state = ScreenState.MENU
text = "0"
SPData = {}

class Button():
    def __init__(self, x,y, image, imageOnClick, scale):
        self.image = pygame.transform.scale(image,(int(image.get_width()*scale), int(image.get_height()*scale)))
        self.imageOnClick = pygame.transform.scale(imageOnClick,(int(imageOnClick.get_width()*scale), int(imageOnClick.get_height()*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        
        self.displayedImage = self.image
        self.clicked = False
        self.action = False #pozwolenie na podjęcie akcji

    def draw(self,screen):

        mouseposition = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouseposition):
            self.displayedImage = self.imageOnClick

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.action = True

        else:
                self.clicked = False
                self.displayedImage = self.image

        screen.blit(self.displayedImage, (self.rect.x,self.rect.y))

class TextInput():
    def __init__(self,x,y,image, parameterstate):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.parameterstate = parameterstate
        self.text = "0"

    def draw(self,screen):

        screen.blit(self.image,(self.rect.x,self.rect.y))

        mouseposition = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouseposition) and pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
        else:
            self.clicked = False
        font = pygame.font.Font(None, 32)

        displayText = font.render(self.text,True,(255,255,255))
        screen.blit(displayText,(self.rect.x,self.rect.y + self.image.get_height()/4))

#--------------------------- OBRAZY -------------------------#
        
BACKGROUND = pygame.image.load(r"repository\images\background.jpg")
MenuTitle = pygame.image.load(r"repository\images\MenuTitle.png")
TopsisTitle = pygame.image.load(r"repository\images\TopsisTitle.png")
RSMTitle = pygame.image.load(r"repository\images\RSMTitle.png")
SPTitle = pygame.image.load(r"repository\images\SPTitle.png")
TabelaPunktow = pygame.image.load(r"repository\images\TabelaPunktow.png")
TextBox = pygame.image.load(r"repository\images\TextBox.png")

TopsisBtnImg = pygame.image.load(r"repository\images\TopsisBtn.png")
TopsisBtnOnClickImg = pygame.image.load(r"repository\images\TopsisBtnOnClick.png")
TopsisBtn = Button(90,185,TopsisBtnImg,TopsisBtnOnClickImg,1)

RSMBtnImg = pygame.image.load(r"repository\images\RSMBtn.png")
RSMBtnOnClickImg = pygame.image.load(r"repository\images\RSMBtnOnClick.png")
RSMBtn = Button(470,185,RSMBtnImg,RSMBtnOnClickImg,1)

SPBtnImg = pygame.image.load(r"repository\images\SPBtn.png")
SPBtnOnClickImg = pygame.image.load(r"repository\images\SPBtnOnClick.png")
SPBtn = Button(90,280,SPBtnImg,SPBtnOnClickImg,1)

UTEBtnImg = pygame.image.load(r"repository\images\UteBtn.png")
UTEtnOnClickImg = pygame.image.load(r"repository\images\UteBtnOnClick.png")
UTEBtn = Button(470,280,UTEBtnImg,UTEtnOnClickImg,1)
        
PodstawowyBtnImg = pygame.image.load(r"repository\images\PodstawowyBtn.png")
PodstawowyBtnOnClickImg = pygame.image.load(r"repository\images\PodstawowyBtnOnClick.png")
PodstawowyBtn = Button(30,410,PodstawowyBtnImg,PodstawowyBtnOnClickImg,1)

RozszerzonyBtnImg = pygame.image.load(r"repository\images\ZaawansowanyBtn.png")
RozszerzonyBtnOnClickImg = pygame.image.load(r"repository\images\ZaawansowanyBtnOnClick.png")
RozszerzonyBtn = Button(500,410,RozszerzonyBtnImg,RozszerzonyBtnOnClickImg,1)

WrocBtnImg = pygame.image.load(r"repository\images\WrocBtn.png")
WrocBtnOnClickImg = pygame.image.load(r"repository\images\WrocBtnOnClick.png")
WrocBtn = Button(30,490,WrocBtnImg,WrocBtnOnClickImg,1)

WyswietlRankingBtnImg = pygame.image.load(r"repository\images\WyswietlRankingBtn.png")
WyswetlRankingBtnOnClickImg = pygame.image.load(r"repository\images\WyswietlRankingBtnOnClick.png")
WyswietlRankingBtn = Button(545,490,WyswietlRankingBtnImg,WyswetlRankingBtnOnClickImg,1)

DodajdostatusquoImg = pygame.image.load(r"repository\images\DodajdostatusquoBtn.png")
DodajdostatusquoOnClickImg = pygame.image.load(r"repository\images\DodajdostatusquoBtnOnClick.png")
DodajdostatusquoBtn = Button(30,400,DodajdostatusquoImg,DodajdostatusquoOnClickImg,1)

DodajdodocelowychImg = pygame.image.load(r"repository\images\DodajdodocelowychBtn.png")
DodajdodocelowychOnClickImg = pygame.image.load(r"repository\images\DodajdodocelowychBtnOnClick.png")
DodajdodocelowychBtn = Button(545,400,DodajdodocelowychImg,DodajdodocelowychOnClickImg,1)

