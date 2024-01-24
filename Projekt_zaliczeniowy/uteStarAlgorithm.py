import numpy as np
from copy import deepcopy
import generalAlgorithm as d


def UTE_Star(X, compartments: np.ndarray, weights : np.ndarray, terms : list):
    compartments_copy = deepcopy(compartments) 
    X_array = X.to_numpy()

    compartments_copy = np.insert(compartments_copy,[0],np.zeros((compartments_copy.shape[0],1)),axis = 1)
    compartments_copy = np.insert(compartments_copy,[compartments.shape[1]+1],np.zeros((compartments_copy.shape[0],1)),axis = 1)

    idx_terms = 0
    for idx, col in enumerate(X_array.transpose()):
        if(any([isinstance(el_col,str) for el_col in col])):
            continue
        if terms[idx_terms] == min:
            compartments_copy[idx_terms,0] = np.min(col)
            compartments_copy[idx_terms,-1] = np.max(col)
        elif terms[idx_terms] == max:
            compartments_copy[idx_terms,-1] = np.min(col)
            compartments_copy[idx_terms,0] = np.max(col)
        idx_terms += 1


    if(np.sum(weights[:,0]) != 1):
        return None
    
    U_ab_list = []
    for idx, row in enumerate(weights):
        compartments_row = list(filter(lambda item: item is not None, compartments_copy[idx]))
        weights_row = list(filter(lambda item: item is not None, row))
        
        u = np.zeros((len(weights_row)-1,2))
        
        n_col_u = u.shape[1] -1

        

        for idx_u, el_u in enumerate(u):
            if terms[idx] == max:
                a = (weights_row[idx_u+1] - weights_row[idx_u])/(compartments_row[idx_u+1] - compartments_row[idx_u])
                b = (weights_row[idx_u] - a * compartments_row[idx_u] )
                u[n_col_u -idx_u,0] = a
                u[n_col_u -idx_u,1] = b
                
            elif terms[idx] == min:
                a = (weights_row[idx_u] - weights_row[idx_u+1])/(compartments_row[idx_u] - compartments_row[idx_u+1])
                b = (weights_row[idx_u] - a * compartments_row[idx_u] )
                u[idx_u,0] = a
                u[idx_u,1] = b              
    

        U_ab_list.append(u)
    U_value = []
    idx_column = 0
    for column in X_array.transpose():
        
        if(any([isinstance(el_col,str) for el_col in column])):
            continue

        compartments_row = list(filter(lambda item: item is not None, compartments_copy[idx_column]))
        compartments_row_reverse = deepcopy(compartments_row)
        compartments_row_reverse.reverse()
        weights_row = list(filter(lambda item: item is not None, weights[idx_column]))
        u_value = []
        
        for el_row in column:
            number_compartments = 0
            if terms[idx_column] == min:
                for idx_element, element in enumerate(compartments_row):
                    if terms[idx_column] == min:
                        if el_row < element or (idx_element == len(compartments_row)-1 and el_row <= element):
                            number_compartments = idx_element - 1
                            break
            elif terms[idx_column] == max:
                for idx_element, element in enumerate(compartments_row_reverse):
                    if el_row < element or (idx_element == len(compartments_row_reverse)-1 and el_row <= element):
                        number_compartments = idx_element - 1
                        break

            u_value.append(el_row*U_ab_list[idx_column][number_compartments,0] + U_ab_list[idx_column][number_compartments,1])    
        idx_column += 1
        U_value.append(u_value)

    
    amount_new_column = len(U_value)
    U_value = np.array(U_value).transpose()

    result = np.array([[np.sum(el) for el in U_value]]).transpose()
    U_value = np.insert(U_value,[U_value.shape[1]],result,axis=1)
    X_array = np.insert(X_array,[X_array.shape[1]],U_value,axis=1)

    name_columns = X.columns.to_numpy()
    data = d.Array2DataFarame(np.append(name_columns,[f"Wartosc u{idx + 1}" if idx != amount_new_column else "Ranking" for idx in range(amount_new_column + 1)]),X_array)
    # data = data.sort_values(by=['Ranking'],ascending= False,ignore_index= True)

    return data



def SetWeights(terms_vector,docelowe_vector,vectors_compartments : np.ndarray):
    n,m = vectors_compartments.shape
    Weights_result = []
    for idx_row, row in enumerate(vectors_compartments):
        if docelowe_vector[idx_row] < np.min(row) or docelowe_vector[idx_row] > np.max(row):
            weights_vector = np.linspace(1/n,0,m).tolist()
            Weights_result.append(weights_vector)
            if terms_vector[idx_row] == max:
                vec = list(vectors_compartments[idx_row])
                vec.reverse()
                vectors_compartments[idx_row] = vec
                
            continue

        for idx_el, el in enumerate(row):
            if docelowe_vector[idx_row] <= el:
                a = np.linspace(0,0.05,m - (idx_el+1))
                b = np.linspace(0.1,1/n,m - (m - (idx_el+1)))
                weights_vector = list(np.insert(b,[0],a,axis = 0))
                weights_vector.reverse()
                break

        Weights_result.append(weights_vector)
        if terms_vector[idx_row] == max:
            vec = list(vectors_compartments[idx_row])
            vec.reverse()
            vectors_compartments[idx_row] = vec
    vectors_compartments = np.delete(vectors_compartments,[0,-1],1)      
    return np.array(Weights_result), vectors_compartments