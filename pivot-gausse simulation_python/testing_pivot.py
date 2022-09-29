import numpy as np
import copy
from scipy.linalg import lu

matrix= np.array([[1,2,0,1,1],[2,1,0,0,1],[-1,-2,-1,1,1],[0,1,1,-1,2],[1,0,0,0,0]])

index=0

def echelonne_sci(matrix):
    p, l, u = lu(matrix)   
    matrix_eche=u     
    """if the initial matrix is type (n,n) """
    return matrix_eche

matrix= echelonne_sci(matrix)

def pivot_index(matrix):
    list_pivot=[]
    for row_index in range(len((matrix))):
        for index in range(len(matrix[row_index])):
            if matrix[row_index][index]!=0:
                list_pivot.append(index)
                break
                
            elif matrix[row_index][index]==0:
                continue
            else:
                print('ERREUR CHECK INITIAL CODE')
    print(list_pivot)
    return list_pivot
pivot_index(matrix)

 
