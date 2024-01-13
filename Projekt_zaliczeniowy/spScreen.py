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

class SP():
    def __init__(self):
        pass
    
    def draw(self, screen):
        screen.blit(repository.SPTitle, (90,30))
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
            repository.WrocBtn.action = False

        if repository.DodajdodocelowychBtn.action == True:
            data.SPDocelowe["Przewyzszenie"].append(float(PrzewyzszeniaInput.text))
            data.SPDocelowe["Wysokosc"].append(float(WysokoscInput.text))
            data.SPDocelowe["Czas"].append(float(CzasInput.text))
            data.SPDocelowe["Dlugosc"].append(float(DlugoscInput.text))
            data.SPDocelowe["Got"].append(float(GotInput.text))
            data.SPDocelowe["TempLato"].append(float(TempLatoInput.text))
            data.SPDocelowe["TempZima"].append(float(TempZimaInput.text))
            data.SPDocelowe["Ocena"].append(float(OcenaGoogleInput.text))
            repository.DodajdodocelowychBtn.action = False

        if repository.DodajdostatusquoBtn.action == True:
            data.SPStatusQuo["Przewyzszenie"].append(float(PrzewyzszeniaInput.text))
            data.SPStatusQuo["Wysokosc"].append(float(WysokoscInput.text))
            data.SPStatusQuo["Czas"].append(float(CzasInput.text))
            data.SPStatusQuo["Dlugosc"].append(float(DlugoscInput.text))
            data.SPStatusQuo["Got"].append(float(GotInput.text))
            data.SPStatusQuo["TempLato"].append(float(TempLatoInput.text))
            data.SPStatusQuo["TempZima"].append(float(TempZimaInput.text))
            data.SPStatusQuo["Ocena"].append(float(OcenaGoogleInput.text))
            repository.DodajdostatusquoBtn.action = False
        
        if repository.WyswietlRankingBtn.action == True:
            data.Ranking =  data.SPFunction()
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
    
    