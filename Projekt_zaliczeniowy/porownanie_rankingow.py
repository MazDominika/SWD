import pandas as pd
import numpy as np
from scipy.stats import spearmanr, kendalltau
import matplotlib.pyplot as plt

import data  


data.SPStatusQuo = {"Wysokosc": [2600], "Przewyzszenie" :[1500], "Dlugosc": [30], "Czas": [700] , "TempZima" : [-25], "TempLato" : [30], "Ocena" :[3], "Got":[60]}
data.SPDocelowe  = {"Wysokosc": [1500], "Przewyzszenie" :[400], "Dlugosc": [10], "Czas": [300] , "TempZima" : [-9], "TempLato" : [12], "Ocena" :[6], "Got":[20]}
data.TopsisWeight = {"Wysokosc": 0.125, "Przewyzszenie" :0.125, "Dlugosc": 0.125, "Czas": 0.125, "TempZima" : 0.125, "TempLato" : 0.125, "Ocena" :0.125, "Got": 0.125}
data.RSMtatusQuo = {"Wysokosc": [2600], "Przewyzszenie" :[1500], "Dlugosc": [30], "Czas": [700] , "TempZima" : [-25], "TempLato" : [30], "Ocena" :[3], "Got":[60]}
data.RSMDocelowe  = {"Wysokosc": [1500], "Przewyzszenie" :[400], "Dlugosc": [10], "Czas": [300] , "TempZima" : [-9], "TempLato" : [12], "Ocena" :[6], "Got":[20]}
data.UteDocelowe = {"Wysokosc": 1500, "Przewyzszenie" :400, "Dlugosc": 10, "Czas": 300, "TempZima" : -9, "TempLato" : 12, "Ocena" :6, "Got": 20}

rsm_ranking = data.RSMFunction()

sp_ranking = data.SPFunction()



rsm_ranking_array = rsm_ranking.iloc[:,3:].to_numpy(float)
sp_ranking_array = sp_ranking.iloc[:,3:].to_numpy(float)
docelowy = np.array([data.RSMDocelowe[key] for key in data.NamesColumnsInGoodOrder],object).transpose()


d_from_rsm = (np.sum((docelowy - rsm_ranking_array[0,:-1])**2))**(1/2)
print("Odległość najlepszego szczytu od punktu docelowego dla metody RSM:", d_from_rsm)
d_from_sp = (np.sum((docelowy - sp_ranking_array[0,:-1])**2))**(1/2)
print("Odległość najlepszego szczytu od punktu docelowego dla metody SP:", d_from_sp)

print("\n")


d_between_method_sp_rsm = np.sum(np.sum((rsm_ranking_array[:4,:-1] - sp_ranking_array[:4,:-1])**2,axis= 1)**(1/2))/4
print("Odległość pomiędzy rankingami RSM oraz SP dla 4 pierwszych miejsc:",d_between_method_sp_rsm)


# spearman_rsm_sp = spearmanr(rsm_ranking_array[:4,-1], sp_ranking_array[:4,-1],axis= 1)
# print(spearman_rsm_sp,"\n\n\n")
print("\n\n")


ute_ranking_unsorted = data.UTEStarFunction()
ute_ranking = ute_ranking_unsorted.sort_values(by=['Ranking'],ascending= False,ignore_index= True)

topsis_ranking_unsorted = data.TopsisFunction()

topsis_ranking = topsis_ranking_unsorted.sort_values(by=['Topsis'], ascending=False, ignore_index= True)



ute_ranking_array = ute_ranking.iloc[:,3:].to_numpy(float)
topsis_ranking_array = topsis_ranking.iloc[:,3:].to_numpy(float)

docelowy = np.min((data.Szczyty).iloc[:,3:].to_numpy(),axis= 0)
d_from_topsis = (np.sum((docelowy - topsis_ranking_array[0,:-1])**2))**(1/2)
print("Odległość najlepszego szczytu od punktu docelowego dla metody Topsis:", d_from_topsis)
d_from_ute = (np.sum((docelowy - ute_ranking_array[0,:-9])**2))**(1/2)
print("Odległość najlepszego szczytu od punktu docelowego dla metody UTE star:", d_from_ute)


print("\n")
d_between_method_topsis_ute = np.sum(np.sum((ute_ranking_array[:4,:-9] - topsis_ranking_array[:4,:-1])**2,axis= 1)**(1/2))/4
print("Odległość pomiędzy rankingami UTE star oraz Topsis dla 4 pierwszych miejsc:",d_between_method_topsis_ute)

print("\n")


spearman_topsis_ute = spearmanr(topsis_ranking_unsorted.loc[:,'Topsis'].to_numpy(), ute_ranking_unsorted.loc[:,"Ranking"].to_numpy())
print("Korelacja wyników uzyskanych metodami UTE star oraz Topsis (spearmanr): ",spearman_topsis_ute)

kendalltau_topsis_ute = kendalltau(topsis_ranking_unsorted.loc[:,'Topsis'].to_numpy(), ute_ranking_unsorted.loc[:,"Ranking"].to_numpy())
print("Korelacja wyników uzyskanych metodami UTE star oraz Topsis (kendalltau): ",kendalltau_topsis_ute)


X_rsm_sp_topsis_ute = ["SP", "RSM", "Topsis", "UTE star"]
Y_rsm_sp_topsis_ute = [d_from_sp, d_from_rsm, d_from_topsis, d_from_ute]

X_d = ["SP - RSM", "Topsis - UTE star"]
Y_d = [d_between_method_sp_rsm, d_between_method_topsis_ute]


fig, ax = plt.subplots(2,1)

ax[0].bar(X_rsm_sp_topsis_ute,Y_rsm_sp_topsis_ute)
ax[0].set_title("Odległość od punktu idelanego/docelowego")

ax[1].bar(X_d, Y_d)
ax[1].set_title("Odległość pomiędzy rankingami")

plt.show()