# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(input):
    count = 0 
    length = len(input)
    for i in input:
        for j in i:
            count = count + 1
            if j >= 'a' and j <= 'z' or j >= 'A' and j <= 'Z':
#                print "alphabet"
                return False
            string = str(j)
            if string.find(".") != -1 :
#                print "Decimal number"
                return False
    if length * length != count:
#        print "not n *n"
        return False
    
    for i in input:
        for j in i:
            count1 = 0
            for k in i:
                if j==k:
#                    print "in j==k"
                    count1 = count1+1
                    if count1>1:
#                        print "recurring numbers in rows"
#                        print j
#                        print k
                        return False
#                print "not in while of rows"
            
    temp = []
    for p in range (0, length):
        temp1 = [q[p] for q in input]
        temp.append(temp1)
#    print temp
        
    for i in temp:
        for j in i:
            count2 = 0
            for k in i:
                if j == k:
#                    print "in j == k in column"
                    count2 = count2 + 1
                    if count2 > 1:
#                        print "recurring numbers in columns"
                        return False
#                        print j
#                        print k
#                        return False
#                print "not in while of rows"

    for i in input:
        for j in i:
            if j>length or j <= 0 :
#                print "Doesnt come under 1-n or is 0"
                return False
                
#    print"You have a perfect Sudoku with you"
    return True
                            
        
                
    
        
    
    




    
    
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False


