import pandas as pd
import generalAlgorithm
import numpy as np
import topsisAlgorithm
import uteStarAlgorithm 
import rsmAlgorithm
import SPAlgorithm




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

NamesColumnsInGoodOrder = ["Wysokosc","Dlugosc","Czas","Przewyzszenie","TempZima","TempLato","Ocena","Got"]
Szczyty = pd.read_excel(r"dataSheet\SZCZYTY.xlsx")

def SPFunction():
    Ranking = SPAlgorithm.SP(Szczyty,3,SPDocelowe,SPStatusQuo,NamesColumnsInGoodOrder)
    if Ranking is not None:
        # return Ranking.iloc[:,:-1]
        return Ranking


def RSMFunction():
    terms_vector = [TopsisMinMaxVector[key] for key in NamesColumnsInGoodOrder]
    A_1 = np.array([RSMtatusQuo[key] for key in NamesColumnsInGoodOrder],object).transpose()
    A_1 = np.insert(A_1,[0],["szczyt status-quo","pasmo status-quo","trasa status-quo"], axis= 1)
    A_0 = np.array([RSMDocelowe[key] for key in NamesColumnsInGoodOrder],object).transpose()
    A_0 = np.insert(A_0,[0],["szczyt docelowe","pasmo docelowe","trasa docelowe"], axis= 1)


    Ranking = rsmAlgorithm.RSM(Szczyty,A_0,A_1,3,terms_vector)
    if Ranking is not None:
        if Ranking.iloc[0,-1] is not None:
            idx_el = 0
            for idx, el in enumerate(Ranking.iloc[:,-1]):
                if el is None:
                    idx_el = idx
                    break
            # return Ranking.iloc[:idx_el,:-1]
            return Ranking.iloc[:idx_el,:]
        else:
            return None
        

def TopsisFunction():
    terms_vector = [TopsisMinMaxVector[key] for key in NamesColumnsInGoodOrder]
    weight_vector = [TopsisWeight[key] for key in NamesColumnsInGoodOrder]
    _ ,Result_OWD_filtered = generalAlgorithm.OWD_with_filter(Szczyty,3, terms_vector)
    nadir = [np.min(x) if terms_vector[idx_x] == max else np.max(x) for idx_x, x in enumerate(generalAlgorithm.DataFrame2Array_without_string(Result_OWD_filtered).transpose())]
    Ranking = topsisAlgorithm.Topsis_method(Szczyty,(3,Szczyty.shape[1]),terms_vector,weight_vector,antyideal_point= nadir)
    if Ranking is not None:
        # return Ranking.iloc[:,:-1]
        return Ranking
    

def UTEStarFunction():

    number = 100
    terms_vector = [UteMinMaxVector[key] for key in NamesColumnsInGoodOrder]
    docelowe_vector = [UteDocelowe[key] for key in NamesColumnsInGoodOrder]
    vectors_compartments = np.array([np.linspace(np.min(col),max(col),number) for col in Szczyty.iloc[:,3:].to_numpy().transpose()])
    weights_vectors, vectors_compartments= uteStarAlgorithm.SetWeights(terms_vector,docelowe_vector,vectors_compartments)
    Ranking = uteStarAlgorithm.UTE_Star(Szczyty,vectors_compartments,weights_vectors,terms_vector)
    if Ranking is not None:
        # return Ranking.iloc[:,:11]
        return Ranking
   


    