import numpy as np
from copy import deepcopy
import generalAlgorithm






def RSM(Y,A_0 : np.ndarray,A_1 : np.ndarray, from_col :int, exceptional_vetor : list):
    new_points_A0,test_A0 = generalAlgorithm.InternalConsistency(deepcopy(A_0),from_col,exceptional_vetor)
    if not test_A0:
        A_0 = new_points_A0


    new_points_A1,test_A1 = generalAlgorithm.InternalConsistency(deepcopy(A_1),from_col,exceptional_vetor)
    if not test_A1:
        A_1 = new_points_A1


    new_points,test = generalAlgorithm.MutualConsistency(deepcopy(A_0),deepcopy(A_1),from_col,exceptional_vetor)
    if not test:
        A_0 = new_points
    
    Y_array = deepcopy(Y).to_numpy()

    P_array = np.zeros((A_0.shape[0],A_1.shape[0]))
    
    for idx_A_0, el_A_0 in enumerate(A_0[:,from_col:]):
        for idx_A_1, el_A_1 in enumerate(A_1[:,from_col:]):
            P = np.prod([np.abs(x - el_A_1[i]) for i, x in enumerate(el_A_0)])
            P_array[idx_A_0,idx_A_1] = P
    Sum_P = np.sum(P_array)
    Omega_array = P_array/Sum_P
    result = []
    for idx_Y, el_Y in enumerate(Y_array[:,from_col:]):
        value_f = 0
        for idx_A_0, el_A_0 in enumerate(A_0[:,from_col:]):
            for idx_A_1, el_A_1 in enumerate(A_1[:,from_col:]):
                flag = True
                for i in range(len(el_A_0)):
                    if el_A_0[i] <= el_A_1[i]:                     
                        if not(el_Y[i] >= el_A_0[i] and el_Y[i] <=el_A_1[i]):
                            flag = False
                            break
                    else:
                        if not(el_Y[i] >= el_A_1[i] and el_Y[i] <=el_A_0[i]):
                            flag = False
                            break 
                if flag == True:
                    d_0 = sum((el_A_0 - el_Y)**2)**(1/2)
                    d_1 = sum((el_A_1 - el_Y)**2)**(1/2)
                    value_f = value_f + Omega_array[idx_A_0,idx_A_1] * (d_0 - d_1)
        result.append(value_f)
    
    result = np.array([result]).transpose()
    result = np.where(result == 0, None, result)
    Y_array = np.append(Y_array,result,axis= 1)

    name_columns = Y.columns.to_numpy()
    data = generalAlgorithm.Array2DataFarame(np.append(name_columns,'RSM'),Y_array)
    data = data.sort_values(by=['RSM'], ascending= True, ignore_index= True)

    return data