#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

def print_abacus(value):
    def get_abacus_output(x):
        if(x == 1):
            y = '|00000****   *|'
            return y
        if(x == 2):
            y = '|00000***   **|'
            return y
        if(x == 3):
            y = '|00000**   ***|'
            return y
        if(x == 4):
            y = '|00000*   ****|'
            return y
        if(x == 5):
            y = '|00000   *****|'
            return y
        if(x == 6):
            y = '|0000   0*****|'
            return y
        if(x == 7):
            y = '|000   00*****|'
            return y
        if(x == 8):
            y = '|00   000*****|'
            return y
        if(x == 9):
            y = '|0   0000*****|'
            return y
        else:
            y = '|00000*****   |'
            return y
 
 #default abacus value   
    abacus = ['|00000*****   |','|00000*****   |','|00000*****   |','|00000*****   |','|00000*****   |','|00000*****   |','|00000*****   |','|00000*****   |','|00000*****   |','|00000*****   |']
    
    i = 0
    j = 0
    list_length = 9
    a = value/10
    b = value%10
    while(a != 0):
        abacus_temp = get_abacus_output(b)
        abacus[list_length-i] = abacus_temp 
        value = value/10
        i = i + 1
        a = value/10
        b = value%10

#if value = 1, a = 0, b = 1 and we need to execute the operation again till b=0 
    if(a/10 == 0):
        abacus_temp = get_abacus_output(b)
        abacus[list_length-i] = abacus_temp 

#print the abacus constructed newly
    while(j<=list_length):
        print(abacus[j])
        j = j + 1
   
   
###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|
