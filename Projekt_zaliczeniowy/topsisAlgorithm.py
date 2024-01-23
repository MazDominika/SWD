import numpy as np
from copy import deepcopy


class Topsis:
    def __init__(self,products, vector_norm : list ) -> None:
        self.products = products 
        self.vector_norm = vector_norm
    
    def norm(self,vector_columns) -> np.ndarray:
        db_array  = self.products.iloc[:,vector_columns].to_numpy()
        v_norm = db_array**2
        v_norm = sum(v_norm)
        v_norm = v_norm**(1/2)
        norm_matrix = db_array/v_norm
        return norm_matrix,v_norm
    
    def norm_with_weight(self,norm_matrix) -> np.ndarray:
        return norm_matrix*self.vector_norm
    
    def ideal_point(self,matrix_norm_with_weight: np.ndarray ,ideal_vector: list)-> list[np.ndarray]:
        ideal_result_vector = []
        antyideal_result_vector = []
        antyideal_vector = [min if x==max else max for x in ideal_vector ]
        for idx_el, el in enumerate(ideal_vector):
            ideal_result_vector.append(el(matrix_norm_with_weight[:,idx_el]))
            antyideal_result_vector.append(antyideal_vector[idx_el](matrix_norm_with_weight[:,idx_el]))
        return [np.array(ideal_result_vector),np.array(antyideal_result_vector)]

    def result_topsic(self,matrix_norm_with_weight: np.ndarray, ideal_point_vector: np.ndarray,antyideal_point_vector: np.ndarray):
        distance_plus = (deepcopy(matrix_norm_with_weight)-ideal_point_vector)**2
        distance_minu = (deepcopy(matrix_norm_with_weight)-antyideal_point_vector)**2
        distance_plus = np.array([(sum(distance_plus.transpose())**(1/2))]).transpose()
        distance_minu = np.array([(sum(distance_minu.transpose())**(1/2))]).transpose()
        
        result = list((distance_minu/(distance_plus+distance_minu)).transpose()[0])
        self.products = self.products.assign(Topsis = result)
        return self.products.sort_values(by=['Topsis'], ascending=False, ignore_index= True)
    


    
def Topsis_method(DataFrame,date_to_count :tuple|list,idela_vector :list,WeigthVector :list = None , antyideal_point :list = None ):

    if np.sum(WeigthVector) != 1:
        return None
    
    topsis = Topsis(DataFrame,WeigthVector)
    if isinstance(date_to_count,tuple):
        norm_matrix, v_norm = topsis.norm(slice(date_to_count[0],date_to_count[1]))
    else:
        norm_matrix, v_norm = topsis.norm(date_to_count)

    if WeigthVector is not None:
        matrix_norm_with_weight = topsis.norm_with_weight(norm_matrix)
    else:
        matrix_norm_with_weight = norm_matrix
    
    if antyideal_point is None:
        ideal,antyideal = topsis.ideal_point(matrix_norm_with_weight,idela_vector)
    else:
        ideal,antyideal = topsis.ideal_point(matrix_norm_with_weight,idela_vector)
        antyideal = antyideal_point/v_norm
    New_Db = topsis.result_topsic(matrix_norm_with_weight,ideal,antyideal)
    return New_Db



def best_worst_product(DataFrame,column_name: str,term):
    value = term(list(DataFrame.loc[:,column_name])) 
    result =DataFrame[DataFrame[column_name] == value] 
    return result
