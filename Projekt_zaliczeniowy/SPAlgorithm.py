import numpy as np
from copy import deepcopy
import generalAlgorithm 


def SP(Szczyty, from_col: int ,SPDocelowe, SPStatusQuo,NamesColumnsInGoodOrder):
    if np.any([len(SPDocelowe[key]) != len(SPStatusQuo[key]) for key in NamesColumnsInGoodOrder]):
        return None
    
    Szczyty_numpy = deepcopy(Szczyty).to_numpy()
    Szczyty_numpy_selected = deepcopy(Szczyty).to_numpy()
    selected_array = []
    flag = False

    
    #Ograniczenie szczytów które wykraczają poza punkty docelowe oraz StatusQuo
    for hills in range(len(Szczyty_numpy)):
        selected_array.append(list(Szczyty_numpy[hills]))
        for pos, name in enumerate(NamesColumnsInGoodOrder):
            for krzywa in range(len(SPDocelowe["Wysokosc"])):
                if not((Szczyty_numpy[hills][pos+from_col] > SPDocelowe[name][krzywa] and Szczyty_numpy[hills][pos+3] < SPStatusQuo[name][krzywa]) or (Szczyty_numpy[hills][pos+3] < SPDocelowe[name][krzywa] and Szczyty_numpy[hills][pos+3] > SPStatusQuo[name][krzywa])):
                    selected_array.pop(-1)
                    flag = True
                    break
            if flag:
                break          
    """
    #Normalizacja punktów do wartości (0,1)
    for elem in range(from_col, len(Szczyty_numpy[0])):
        column = [row[elem] for row in Szczyty_numpy]
        for hill in range(len(Szczyty_numpy)):
            #Szczyty_numpy[hill][elem] = (Szczyty_numpy[hill][elem] - np.min(column))/(np.max(column)-np.min(column))
            pass
        for krzywa in range(len(SPDocelowe['Wysokosc'])):
            docelowe_items = list(SPDocelowe.items())
            status_items = list(SPStatusQuo.items())
            key, value = docelowe_items[elem-3]
            key2, value2 = status_items[elem-3]
            #SPDocelowe[key][krzywa] = (value[krzywa] - np.min(column))/(np.max(column)-np.min(column))
            #SPStatusQuo[key2][krzywa] = (value2[krzywa] - np.min(column))/(np.max(column)-np.min(column))
            Szczyty_numpy[hill][elem] = (Szczyty_numpy[hill][elem] - SPStatusQuo[key2][krzywa])/(SPDocelowe[key][krzywa]-SPStatusQuo[key2][krzywa])
            SPDocelowe[key][krzywa] = (value[krzywa] - SPStatusQuo[key2][krzywa])/(SPDocelowe[key][krzywa]-SPStatusQuo[key2][krzywa])
            SPStatusQuo[key2][krzywa] = (value2[krzywa] - SPStatusQuo[key2][krzywa])/(SPDocelowe[key][krzywa]-SPStatusQuo[key2][krzywa])
    """
    points = [[] for key in range(len(SPDocelowe['Wysokosc']))]
    d = np.zeros(len(NamesColumnsInGoodOrder))
    distance = 0
    curr_distance = []

    #Wyznaczenie krzywej
    for krzywa in range(len(SPDocelowe["Wysokosc"])):
        docelowy = list(val[krzywa] for val in SPDocelowe.values())
        quo = list(val[krzywa] for val in SPStatusQuo.values())
        points[krzywa].append(np.append(docelowy,1))
        points[krzywa].append(np.append(quo,0))
        
        for j in range(len(NamesColumnsInGoodOrder)-1): # j

            for num, val in enumerate(NamesColumnsInGoodOrder): # i
                d[num] = (quo[num] - docelowy[num])/2
                if j >= num:
                    quo[num] = quo[num] - d[num]
                    docelowy[num] = docelowy[num] + d[num]
                else:
                    quo[num] = quo[num]
                    docelowy[num] = docelowy[num]
            
            curr_distance.append(np.linalg.norm(d))
            points[krzywa].append(docelowy)
            points[krzywa].append(quo)
            

            
        
        #Wyliczenie odległości między punktami, dodanie wartości
        distance = sum(arr for arr in curr_distance)
        for arr in range(len(curr_distance)):
            curr_distance[arr] = arr/distance

        normali = []
        normali.append(1)
        normali.append(0)
        for point in range(len(curr_distance)):
            normali.append(normali[point]-curr_distance[point])
            normali.append(normali[point+1]-curr_distance[point])

        #Wyznaczenie odległości punktow do prostej          
        result = []
        print("ARRAY SEL: ",selected_array[0])
        print("POINTS: ", points[krzywa])
        for hills in range(len(selected_array)):
            add = 0
            min_value = 10000
            for point in range(len(points[0])):
                for element in range(3,len(selected_array[0])):
                    add += np.power(selected_array[hills][element] - points[krzywa][point][element-3],2)
                if np.sqrt(add) < min_value:
                    min_value = np.sqrt(add)
            result.append(min_value)    

        print(result)
    #Dodanie dodatkowej kolumny do DataFrame
    result = np.array([result]).transpose()
    selected_array = np.append(selected_array,result,axis=1)
    
    name_columns = Szczyty.columns.to_numpy()
    data = generalAlgorithm.Array2DataFarame(np.append(name_columns,'SP'),np.array(selected_array))
    print(data)
    data = data.sort_values(by=['SP'])

    return data