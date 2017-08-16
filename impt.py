a = [[1,2,3],[4,5,6],[7,8,9]]
c = []
for j in range (0,3):
    b = [i[j] for i in a]
    print (b)
    c.append(b)
print (c)
