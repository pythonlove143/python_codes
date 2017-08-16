# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(input):
    i = 0
    count = 0
    m = 0
    l = 0
    c = []
    length = len(input)

    if input == []:
        return True
    
    for m in range (0,length):
#        print "new addition"
        b = [l[m] for l in input]
        if(len(b) != len(l)):
            return False
        if b:
            c.append(b)
#            print c
    if c != input:
#        print "are we here"
        return False
    return True
        

    # Your code here
    
print symmetric([[1]])
#   True

print symmetric([[1,2,3]])
#   False

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False
