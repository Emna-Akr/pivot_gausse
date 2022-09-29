def pivot_g(matrix_st,matrix_nd,):
    for i in range(len(a)):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')  
            for j in range(len(a)):
                if i != j:
                    ratio = a[j][i]/a[i][i]
                    for k in range(len(a[0])):
                        a[j][k] = a[j][k] - ratio * a[i][k]

#These next 2 lines need fixing  
    for i in range(len(a)):
    a[i] = (v/a[i][i] for v in a[i])        

    return a