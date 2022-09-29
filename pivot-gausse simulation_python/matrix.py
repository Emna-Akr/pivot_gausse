import numpy as np
import copy
from scipy import linalg
from scipy.linalg import lu,solve_triangular
"""

accessing the colums of a matrix 

METHOD 1:

for row in range(len(matrix)):
    for colum in range(len(np.transpose(matrix)))
    print(matrix[row][colum])

METHOD 2:

matrix_new =np.transpose(matrix)
matrix[]

"""
def echange(matrix,line_old,line_new):
    tempo=copy.deepcopy(matrix[line_old]) # deepcopy to create a look-alike undependent from original 
    matrix[line_old]=matrix[line_new]
    matrix[line_new]=tempo
    return matrix

def multiplication(matrix,line,factor):
    matrix[line]=factor*matrix[line]
    return matrix

def transvection(matrix,line_st,line_nd,factor):
    if line_st!=line_nd:
        matrix[line_st]=matrix[line_st]+factor*matrix[line_nd]
    return matrix

""" THE IDEAL WAY TO PROCEED FURTHER SCIPY LIBRARY BUILT IN FUNCTION for more 
    info:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lu.html
""" 
def echelonne_sci(matrix):
    p, l, u = lu(matrix)   
    matrix_eche=u     
    """if the initial matrix is type (n,n) """
    return matrix_eche

"""
ESSAI QUESTIOON 3 WITH A MATHMATICAL VERSION 

def echelonne(matrix_st,matrix_nd):
    
    if len(matrix_st)=len(matrix_nd):
        for row in range(len(A1)):
            for colum in range(len(np.transpose(matrix)))
                matrix_st[row][colum]
            break 
#def need more info ----- EXPLANATION ----- MATHMATICAL METHOD 
""" 

def pivot_index(matrix):
    list_pivot=[]
    matrix= echelonne_sci(matrix)
    for row_index in range(len((matrix))): #the treatment will be by per row 
        for index in range(len(matrix[row_index])):# we'll be counting the zeros in every row until getting any diffrent value 
            if matrix[row_index][index]!=0: # to reduce time pivot value will get a zero if the matrix doesn't
                list_pivot.append(index)#every time the nested loop gets a pivot value it will be added to the list 
                break     # once the condition is satisfyed the loop would break allowing the rest of the programm to proceed functioning 
                          # won't be stuck on repeat in the for loop 
            elif matrix[row_index][index]==0:
                continue # continuing will allow the loop to proceed to the next stage so the index counting wont stop  
            else:
                print('ERREUR CHECK INITIAL CODE') # not sure if it will happen but if there is a miscalculation the code will show an error .... JUST IN CASE 
    print(list_pivot)
    return list_pivot
    
    
def rang(matrix):
    if echelonne_sci(matrix)!=0:
        matrix_eche=echelonne_sci(matrix)
        rang_matrix=len(matrix_eche)
    return rang_matrix

def inverse(matrix): #square matrix only 
    if len(matrix)==len(np.transpose(matrix)): #conditioning for a squared matrix
        if np.linalg.det(matrix)==0:  # a numpy predefined function 
            inversible= True
    if np.diag(echelonne_sci(matrix))==linalg.eigvals(matrix): # eigvals gets the eigen values of a squared matrix 
        inversible=True
    if inversible==True: #boolean condition to only get a return valu if the statement is logically true 
        matrix_inverse=np.linalg.inv(matrix)
    else:
        print('Matrix not inversible')
    return matrix_inverse


# TO CALCULATE A MATRIX DETERMINANT use the pre defined module in 
# numpy library specifically Linear algebra part using np.linalg.det
# FOR MORE INFO https://numpy.org/devdocs/reference/routines.linalg.html
# https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html
# WELL THIS SURE IS FUN XD

def solv_sci(matrix_st, matrix_nd): 
    if len(matrix_st)==len(np.transpose(matrix_st)):
        rang(matrix_st)==len(matrix_st) #verification if matrix is reduced meanin; vectors are undependant 
        #square matrix only #the matrix have to be linear
        sol_vector =linalg.solve(matrix_st, matrix_nd)
        print('sol_vector',sol_vector)# a solution array 
    elif len(matrix_st)!=len(np.transpose(matrix_st)):#(M,N) type matrix so to reduce compilation time we have alredy identifyed when a matrix is square and got out a result so now to the non square matrix :) 
        #(M, N) matrix # least-squares Method when the matrix is linearly dependant or if not square or if not full-rank
        p, res, rnk, s=np.linalg.lstsq(matrix_st,matrix_nd)
        #where "p : Least-squares solution" "res:residues" "rnk: rank" "s:Singular values"
        print('solution: ',p)
    else:
        print('ERREUR: NO SOLUTION TO THE ABOVE SYSTEM')

"""DOCUMENTATION ON 
        #numpy.linalg.solve(a,b) :https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html
        #numpy.linalg.lstsq(a, b, rcond='warn') :https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq
"""
def EXERCICE2(matrix_st,matrix_nd):
    p, l, u = lu(matrix_nd) #any type of a random matrix would do # NB: testing on matrix_nd
    """p:Permutation matrix, l:Lower triangular or trapezoidal matrix, u:Upper triangular or trapezoidal matrix"""
    print('U: ',u,'\n L:',l)
    if len(matrix_st)==len(np.transpose(matrix_st)): 
        SystemeTriangulaireSup=solve_triangular(matrix_st,matrix_nd, lower=False) #SQUARE MATRIX ONLY
        SystemeTriangulaireInf=solve_triangular(matrix_st,matrix_nd, lower=True) #SQUARE MATRIX ONLY
    print('inf',SystemeTriangulaireInf,'\nsup',SystemeTriangulaireSup)
    
    return l,u 
#More info on solve_triangular IN SCIPY LIBRARY :
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_triangular.html


            
#def RESOLUTION_TIME(matrix):
#    if len(np.transpose(matrix))==100 # verification if matrix holds 100 row   
#        for i in range(26) :
#            
#        for i in range(26) :
#            
#        for i in range(26) :
# Need more info to proceed     
        


""" Total mishaps   1/ MATHMATICAL PROCEEDURE TO GET ROW ECHELON FORM QUESTION 3 EXERCICE 1 ---> WITHOUT USING THE SCIPY LIBRARY 
                   2/ALGORITHMICALLY  CALCULATING THE PROCESS TIME ---> IT CAN BE EASILY OBSERVED THOUGH 
                  3/NEED FOR A MORE THROUGHOUT EXPLANATION FOR WHAT WAS DEMANDED ON QUESTION 4 EXERCICE 2 TO EXECUTE THE TIME RESOLUTION FUNCTION 
"""
