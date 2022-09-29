#main matrix 

#TESTING MATRIXES
import numpy as np 
from matrix import *

A1= np.array([[1,2,0,1,1],[2,1,0,0,1],[-1,-2,-1,1,1],[0,1,1,-1,2],[1,0,0,0,0]])

A2= np.array([[1,2,1,2,3],[1,3,1,2,0],[0,1,0,-3,0]])

A3= np.array([[1,2,1,1],[0,1,1,0],[0,0,0,1]])

B1= np.matrix('2 1 -1')

B2= np.matrix('2 1 1')

print('before exchane',A1)

#answer to question 1.

#echange(A1,0,2)

#multiplication(A1,3,2)    

#transvection(A1,1,4,4)

#answer to question 2.

"""
IT would be sufficient to call any needed function after transposing
it to manipulate the rows; check the comment in the matrix.py file 

"""

#answer to question 3.

#echelonne_sci(A1)

#inverse(A3)
## just call for any demanded function from the matrix.py file after checking code to get the names XD