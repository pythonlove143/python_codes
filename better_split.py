# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source,splitlist):
    tempstrsplit = []
    pos = 0
    count = 0
    i = 0
    temp = 0
    splitlength = 0
    strlength = 0
    
    tempsource = source
    
    while(pos != -1):
        #print ("pos", pos)
        pos = source.find(splitlist[0],pos)
        if pos == -1:
            break
        count = count + 1
        pos = pos + 1
    #print count
    
    while i<=count:
        pos = 0
        pos = tempsource.find(splitlist[0],pos)
        if pos == -1:
            if(tempsource != "" and tempsource != source):
                tempstrsplit.append(tempsource)
                break
        temp = tempsource[0:pos]
        #print temp
        if temp != "":
            tempstrsplit.append(temp)
        pos = pos+1
        tempsource = tempsource[pos:]
        #print tempsource
        i = i+1
#    print (tempstrsplit)
    
    i = 0
    j =1
    splitlength = len(splitlist)
    strlength = len(tempstrsplit)
    while j<splitlength:
        while i<strlength:
#            print ("entering j loop, j = , i = ", j,i)
            #print ("splitlist[j]", splitlist[j])
#            print ("tempstrsplit[i]", tempstrsplit[i])
            pos = tempstrsplit[i].find(splitlist[j])
            if pos != -1:
#                print ("entering the if part")
                temp1 = tempstrsplit[i][0:pos]
                temp2 = tempstrsplit[i][(pos+1):]
#                print ("temp1 = ", temp1)
#                print ("temp2 = ", temp2)
                tempstrsplit.pop(i)
                if temp2 != "" and temp2.find(splitlist[j]) == -1:
                    tempstrsplit.insert(i,temp2)
                if temp1 != "" and temp1.find(splitlist[j]) == -1:
                    tempstrsplit.insert(i,temp1)
                strlength = len(tempstrsplit)
#                print ("strlength = ",strlength)
                i = i+1
            else:
#                print ("pos is -1")
                i = i+1
            if i == strlength:
                i = 0
                j = j+ 1
                if j>splitlength:
                    break
                break
                    
 
    return (tempstrsplit)
    
out = split_string("This is a test-of the,string separation-code!"," ,!-")
print (out)
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print (out)
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print (out)
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
