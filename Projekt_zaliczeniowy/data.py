import pandas as pd

SPStatusQuo = {"Wysokosc": [], "Przewyzszenie" :[], "Dlugosc": [], "Czas": [] , "TempZima" : [], "TempLato" : [], "Ocena" :[], "Got":[]}
SPDocelowe  = {"Wysokosc": [], "Przewyzszenie" :[], "Dlugosc": [], "Czas": [] , "TempZima" : [], "TempLato" : [], "Ocena" :[], "Got":[]}

TopsisPodstawowyVector = {"Wysokosc": min, "Przewyzszenie" :  min, "Dlugosc":  min, "Czas":  min, "TempZima" : max, "TempLato" : min, "Ocena" : max, "Got":  min}
TopsisZaawansowanyVector = {"Wysokosc": max, "Przewyzszenie" : max, "Dlugosc": max, "Czas": max, "TempZima" : max, "TempLato" : min, "Ocena" : max, "Got": max}
TopsisMinMaxVector = TopsisPodstawowyVector
TopsisWeight = {"Wysokosc": 0.125, "Przewyzszenie" :0.125, "Dlugosc": 0.125, "Czas": 0.125, "TempZima" : 0.125, "TempLato" : 0.125, "Ocena" :0.125, "Got": 0.125}

RSMtatusQuo = {"Wysokosc": [], "Przewyzszenie" :[], "Dlugosc": [], "Czas": [] , "TempZima" : [], "TempLato" : [], "Ocena" :[], "Got":[]}
RSMDocelowe  = {"Wysokosc": [], "Przewyzszenie" :[], "Dlugosc": [], "Czas": [] , "TempZima" : [], "TempLato" : [], "Ocena" :[], "Got":[]}

UtePodstawowyVector = {"Wysokosc": min, "Przewyzszenie" :  min, "Dlugosc":  min, "Czas":  min, "TempZima" : max, "TempLato" : min, "Ocena" : max, "Got":  min}
UteZaawansowanyVector = {"Wysokosc": max, "Przewyzszenie" : max, "Dlugosc": max, "Czas": max, "TempZima" : max, "TempLato" : min, "Ocena" : max, "Got": max}
UteMinMaxVector = TopsisPodstawowyVector
UteDocelowe = {"Wysokosc": 0, "Przewyzszenie" :0, "Dlugosc": 0, "Czas": 0, "TempZima" : 0, "TempLato" : 0, "Ocena" :0, "Got": 0}

Ranking = None

def SPFunction():
    pass

def RSMFunction():
    pass

def TopsisFunction():
    pass

def UTEStarFunction():
    pass