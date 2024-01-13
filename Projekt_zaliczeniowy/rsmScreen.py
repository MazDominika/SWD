import pygame
import repository
import data

pygame.init()
repository.text = "0"
WysokoscInput = repository.TextInput(280,170,repository.TextBox,repository.SetParametersState.WYSOKOSC)
PrzewyzszeniaInput = repository.TextInput(280,225,repository.TextBox,repository.SetParametersState.PRZEWYZSZENIA)
DlugoscInput = repository.TextInput(280,275,repository.TextBox,repository.SetParametersState.DLUGOSC)
CzasInput = repository.TextInput(280,330,repository.TextBox,repository.SetParametersState.CZAS)
OcenaGoogleInput = repository.TextInput(690,170,repository.TextBox,repository.SetParametersState.OCENA_GOOGLE)
GotInput = repository.TextInput(690,225,repository.TextBox,repository.SetParametersState.GOT)
TempLatoInput = repository.TextInput(690,275,repository.TextBox,repository.SetParametersState.TEMP_LATO)
TempZimaInput = repository.TextInput(690,330,repository.TextBox,repository.SetParametersState.TEMP_ZIMA)

class RSM():
    def __init__(self):
        pass
    
    def draw(self, screen):
        screen.blit(repository.RSMTitle, (90,30))
        screen.blit(repository.TabelaPunktow, (15,150))
        repository.WrocBtn.draw(screen)
        repository.WyswietlRankingBtn.draw(screen)
        repository.DodajdodocelowychBtn.draw(screen)
        repository.DodajdostatusquoBtn.draw(screen)

        WysokoscInput.draw(screen)
        PrzewyzszeniaInput.draw(screen)
        DlugoscInput.draw(screen)
        CzasInput.draw(screen)
        OcenaGoogleInput.draw(screen)
        GotInput.draw(screen)
        TempLatoInput.draw(screen)
        TempZimaInput.draw(screen)
        
        if  repository.WrocBtn.action == True:
            repository.state = repository.ScreenState.MENU
            data.RSMDocelowe = {"Wysokosc": [], "Przewyzszenie" :[], "Dlugosc": [], "Czas": [] , "TempZima" : [], "TempLato" : [], "Ocena" :[], "Got":[]}
            data.RSMtatusQuo = {"Wysokosc": [], "Przewyzszenie" :[], "Dlugosc": [], "Czas": [] , "TempZima" : [], "TempLato" : [], "Ocena" :[], "Got":[]}
            repository.WrocBtn.action = False

        if repository.DodajdodocelowychBtn.action == True:
            data.RSMDocelowe["Przewyzszenie"].append(float(PrzewyzszeniaInput.text))
            data.RSMDocelowe["Wysokosc"].append(float(WysokoscInput.text))
            data.RSMDocelowe["Czas"].append(float(CzasInput.text))
            data.RSMDocelowe["Dlugosc"].append(float(DlugoscInput.text))
            data.RSMDocelowe["Got"].append(float(GotInput.text))
            data.RSMDocelowe["TempLato"].append(float(TempLatoInput.text))
            data.RSMDocelowe["TempZima"].append(float(TempZimaInput.text))
            data.RSMDocelowe["Ocena"].append(float(OcenaGoogleInput.text))
            repository.DodajdodocelowychBtn.action = False

        if repository.DodajdostatusquoBtn.action == True:
            data.RSMtatusQuo["Przewyzszenie"].append(float(PrzewyzszeniaInput.text))
            data.RSMtatusQuo["Wysokosc"].append(float(WysokoscInput.text))
            data.RSMtatusQuo["Czas"].append(float(CzasInput.text))
            data.RSMtatusQuo["Dlugosc"].append(float(DlugoscInput.text))
            data.RSMtatusQuo["Got"].append(float(GotInput.text))
            data.RSMtatusQuo["TempLato"].append(float(TempLatoInput.text))
            data.RSMtatusQuo["TempZima"].append(float(TempZimaInput.text))
            data.RSMtatusQuo["Ocena"].append(float(OcenaGoogleInput.text))
            repository.DodajdostatusquoBtn.action = False
        
        if repository.WyswietlRankingBtn.action == True:
            data.Ranking = data.RSMFunction()
            repository.state = repository.ScreenState.RANKING
            repository.WyswietlRankingBtn.action = False

#---------------------- ZMIANA STANU JAKO SKUTEK KLIKNIECIA------------------
        if PrzewyzszeniaInput.clicked == True:
            repository.setparametersstate = repository.SetParametersState.PRZEWYZSZENIA
            repository.text = ""
        if WysokoscInput.clicked == True:
            repository.setparametersstate = repository.SetParametersState.WYSOKOSC
            repository.text = ""
        if DlugoscInput.clicked == True:
            repository.setparametersstate = repository.SetParametersState.DLUGOSC
            repository.text = ""
        if CzasInput.clicked == True:
            repository.setparametersstate = repository.SetParametersState.CZAS
            repository.text = ""
        if OcenaGoogleInput.clicked == True:
            repository.setparametersstate = repository.SetParametersState.OCENA_GOOGLE
            repository.text = ""
        if GotInput.clicked == True:
            repository.setparametersstate = repository.SetParametersState.GOT
            repository.text = ""
        if TempLatoInput.clicked == True:
            repository.setparametersstate = repository.SetParametersState.TEMP_LATO
            repository.text = ""
        if TempZimaInput.clicked == True:
            repository.setparametersstate = repository.SetParametersState.TEMP_ZIMA
            repository.text = ""

#------------------------------ UZUPELNIANIE TEKSTEM ----------------------------
        if repository.setparametersstate == repository.SetParametersState.PRZEWYZSZENIA:
            PrzewyzszeniaInput.text = repository.text
        if repository.setparametersstate == repository.SetParametersState.WYSOKOSC:
            WysokoscInput.text = repository.text
        if repository.setparametersstate == repository.SetParametersState.DLUGOSC:
            DlugoscInput.text = repository.text
        if repository.setparametersstate == repository.SetParametersState.CZAS:
            CzasInput.text = repository.text
        if repository.setparametersstate == repository.SetParametersState.OCENA_GOOGLE:
            OcenaGoogleInput.text = repository.text
        if repository.setparametersstate == repository.SetParametersState.GOT:
            GotInput.text = repository.text
        if repository.setparametersstate == repository.SetParametersState.TEMP_ZIMA:
            TempZimaInput.text = repository.text
        if repository.setparametersstate == repository.SetParametersState.TEMP_LATO:
            TempLatoInput.text = repository.text
    