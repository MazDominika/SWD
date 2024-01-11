import pygame
import repository
import data

pygame.init()

WysokoscInput = repository.TextInput(280,170,repository.TextBox,repository.SetParametersState.WYSOKOSC)
PrzewyzszeniaInput = repository.TextInput(280,225,repository.TextBox,repository.SetParametersState.PRZEWYZSZENIA)
DlugoscInput = repository.TextInput(280,275,repository.TextBox,repository.SetParametersState.DLUGOSC)
CzasInput = repository.TextInput(280,330,repository.TextBox,repository.SetParametersState.CZAS)
OcenaGoogleInput = repository.TextInput(690,170,repository.TextBox,repository.SetParametersState.OCENA_GOOGLE)
GotInput = repository.TextInput(690,225,repository.TextBox,repository.SetParametersState.GOT)
TempLatoInput = repository.TextInput(690,275,repository.TextBox,repository.SetParametersState.TEMP_LATO)
TempZimaInput = repository.TextInput(690,330,repository.TextBox,repository.SetParametersState.TEMP_ZIMA)

class Topsis():
    def __init__(self):
        pass
    
    def draw(self, screen):
        screen.blit(repository.TopsisTitle, (90,30))
        screen.blit(repository.TabelaPunktow, (15,150))
        repository.WrocBtn.draw(screen)
        repository.WyswietlRankingBtn.draw(screen)
        repository.PodstawowyBtn.draw(screen)
        repository.RozszerzonyBtn.draw(screen)

        WysokoscInput.draw(screen)
        PrzewyzszeniaInput.draw(screen)
        DlugoscInput.draw(screen)
        CzasInput.draw(screen)
        OcenaGoogleInput.draw(screen)
        GotInput.draw(screen)
        TempLatoInput.draw(screen)
        TempZimaInput.draw(screen)

        if repository.WrocBtn.action == True:
            repository.state = repository.ScreenState.MENU
            repository.WrocBtn.action = False
        
        if repository.PodstawowyBtn.action == True:
            data.TopsisMinMaxVector = data.TopsisPodstawowyVector
            repository.PodstawowyBtn.action = False

        if repository.RozszerzonyBtn.action == True:
            data.TopsisMinMaxVector = data.TopsisZaawansowanyVector
            repository.RozszerzonyBtn.action = False

        if repository.WyswietlRankingBtn.action == True:
            data.TopsisWeight["Przewyzszenie"] = (float(PrzewyzszeniaInput.text))
            data.TopsisWeight["Wysokosc"] = (float(WysokoscInput.text))
            data.TopsisWeight["Czas"] = (float(CzasInput.text))
            data.TopsisWeight["Dlugosc"] = (float(DlugoscInput.text))
            data.TopsisWeight["Got"] = (float(GotInput.text))
            data.TopsisWeight["TempLato"] = (float(TempLatoInput.text))
            data.TopsisWeight["TempZima"] = (float(TempZimaInput.text))
            data.TopsisWeight["Ocena"] = (float(OcenaGoogleInput.text))
            data.TopsisFunction()
            repository.state = repository.ScreenState.RANKING

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
    