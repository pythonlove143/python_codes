# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(A):
    
    i = 0
    j= 0 
    m = 0
    l = 0
    c = []
    length = len(A)

    if A == []:
        return True
    
    for m in range (0,length):
        b = [l[m] for l in A]
        if(len(b) != len(l)):
            return False
        if b:
            c.append(b)
    
    while(i<length):
        while(j<length):
            if(c[i][j] != -A[i][j]):
                return False
            j = j+1
        i = i+1
        
    return True


# Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False

print antisymmetric([])

print antisymmetric([[0,2],
                    [-2,0]])


