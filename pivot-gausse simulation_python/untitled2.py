import numpy as np
import copy
from scipy.linalg import lu

matrix= np.array([[1,2,1,2,3],[1,3,1,2,0],[0,1,0,-3,0]])

index=0

def echelonne_sci(matrix):
    p, l, u = lu(matrix)   
    matrix_eche=u     
    """if the initial matrix is type (n,n) """
    return matrix_eche

matrix= echelonne_sci(matrix)
print(matrix)
print('________________')


def pivot_index(matrix):
    for row_index in range(len((matrix))):
        for index in range(len(matrix[row_index])):
            print(matrix[row_index][index])
            if matrix[row_index][index]!=0:
                print('if there is no zero index = ',index)
                pivot_indexation=index
                print('_____________________________ pivot_indexation=',pivot_indexation,'_____________________________')     
                break
                
            elif matrix[row_index][index]==0:
                print('if index is a zero keep counting ',index)
                print(matrix[row_index][index])
            else:
                print('dk')
                return print('ERREUR CHECK CODE')
      
    return pivot_indexation 
pivot_index(matrix)

 
