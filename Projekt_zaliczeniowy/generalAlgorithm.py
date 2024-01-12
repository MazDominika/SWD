import pandas as pd
from copy import deepcopy
import numpy as np




def DataFrame2Array_without_string(DataFrame):
    array = DataFrame.to_numpy()
    for i in range(array.shape[1]):
        if not isinstance(array[1,i],str):
            return array[:,i:]
    return None

def Array2DataFarame(name_columns : np.ndarray, Data : np.ndarray):
    data = {}
    for idx, el in enumerate(Data.transpose()):
        data[name_columns[idx]] = el
    data = pd.DataFrame(data)

    return data

def norm(Xarray : np.ndarray) -> np.ndarray:
        v_norm = Xarray**2
        v_norm = sum(v_norm)
        v_norm = v_norm**(1/2)
        norm_matrix = Xarray/v_norm
        
        return norm_matrix

def OWD_with_filter(X, from_col = None, expectional_vector : list = None):
    if from_col is None:
        from_col = 1
    
    is_numpy = False
    if not isinstance(X, np.ndarray):
        X_array = X.to_numpy()
    else:
        X_array = X
        is_numpy = True
    
    Sub_X_array = deepcopy(X_array)
    if from_col != 0:
        X_array[:,from_col:] = norm(X_array[:,from_col:])
    else:
        X_array = norm(X_array[:,from_col:])
    
    

    if expectional_vector is not None:
        if len(expectional_vector) != X_array.shape[1] - from_col:
            print(len(expectional_vector),X_array.shape[1] - from_col )
            print("zła długość wektora")
            return None
        for idx , el in enumerate(expectional_vector):
            if el == max:
                X_array[:,from_col+idx] = np.ones((1,X_array.shape[0])) - X_array[:,from_col+idx]

    n = X_array.shape[0]
    
    P = []
    P_el = []
    if n == 1:
        P_el.append(Sub_X_array[0,:])
        return P_el, X
    
    while n > 1:
        i = 0
        Y = X_array[i,from_col:]
        j = i+1
        while j < n:
            if all([True if Y[idx] <= arr2_el else False for idx, arr2_el in enumerate(X_array[j,from_col:])]):
                X_array = np.delete(X_array,j,axis=0)
                Sub_X_array = np.delete(Sub_X_array,j,axis=0)
                n -= 1
            elif all([True if Y[idx] >= arr2_el else False for idx, arr2_el in enumerate(X_array[j,from_col:])]):
                Y = X_array[j,from_col:]
                X_array = np.delete(X_array,i,axis=0)
                Sub_X_array = np.delete(Sub_X_array,i,axis=0)
                i = j - 1
                n -= 1
            else:
                j += 1
        

        P.append(tuple(Y))
        P_el.append(Sub_X_array[i,:])
        delete_list = []
        for idx, el in enumerate(X_array):
            if all([True if Y[idx_el] <= arr2_el else False for idx_el, arr2_el in enumerate(el[from_col:])]):
                delete_list.append(idx)
                n -= 1
        
        X_array = np.delete(X_array, delete_list,axis=0)
        Sub_X_array = np.delete(Sub_X_array,delete_list,axis=0)

        if X_array.shape[0] == 1:
            P.append(X_array[0])
            P_el.append(Sub_X_array[0])


    if is_numpy:
        return P_el, np.array(P_el)
    
    name_columns = X.columns.to_numpy()
    data = Array2DataFarame(name_columns,np.array(P_el))
        
    return P_el, data


def InternalConsistency(points, from_col: int, exceptional_vetor : list):
    n = points.shape
    new_points = OWD_with_filter(points,from_col,exceptional_vetor)[1]
    new_n = new_points.shape
    if n == new_n:
        return new_points, True
    else:
        return new_points, False

def MutualConsistency(X,Y, from_col : int, exceptional_vetor : list):
    if not isinstance(X, np.ndarray):
        X_array = X.to_numpy()
    else:
        X_array = X
    if not isinstance(Y,np.ndarray):
        Y_array = Y.to_numpy()
    else:
        Y_array = Y
    
    to_delete = []
    for idx, el in enumerate(X_array):
        points_to_test = np.append(Y_array,[el],axis=0)
        new_points = OWD_with_filter(points_to_test,from_col,exceptional_vetor)[1]
        if (new_points[-1] != points_to_test[-1]).all() and new_points.shape[1] >= points_to_test.shape[1]:
            to_delete.append(idx)

    Sub_X_array = np.delete(X_array,to_delete,axis=0)

    if Sub_X_array.shape == X_array.shape:
        return Sub_X_array, True
    else:
        return Sub_X_array, False

