# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible 
# algorithm or even language of the clear text message, one could perform 
# frequency analysis. This process could be described as simply counting 
# the number of times a certain symbol occurs in the given text. 
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains 
# the lowercase letters a-z. 
# As output you should return a list of the normalized frequency 
# for each of the letters a-z. 
# The normalized frequency is simply the number of occurrences, i, 
# divided by the total number of characters in the message, n.

def freq_analysis(message):
    i = 0
    j = 0
    p = 0
    q = 0
    l = 0
    u = 0
    v = 0
    w = 0
    temp = []
    temp2 = []
    temp3 = []
    freq_list = []
    alpbt=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    length = len(message)
    lengthalpbt = len(alpbt)
    input = [[] for s in range(length)]
#    input = []
    while(i<length):
        j = 0
        count = 0
        while(j<length):
#            print "i",i, message[i]
#            print "j",j, message[j]
            if(message[i] == message[j]):
                count = count + 1
            j = j+1
#        print "count", count
        temp.append(count)
        i = i+1
    
    while(p<length):
        while(q<length):
            if (message[p] == message[q]):
#                print "entered"
#                print "temp[i]", temp[p]
#                print "temp[j]", temp[q]
                temp[p] = temp[q]
            q = q+1
        p = p+1
    
    while(l<length):
        temp[l] = (temp[l] * 1.0)/length
        temp2 = [message[l], temp[l]]
        input[l].append(temp2)
        l = l+1
        
#    print "temp", temp
#    print "input", input
    
#    print freq_list
    
    ##
    # Your code here
    ##
    #return freq_list
    
    while(v<lengthalpbt):
        u = 0
        while(u<length):
#            print "u", u
#            print"input[u][0]", input[u][0]
#            print"alpbt[v]", alpbt[v]
            temp3 = input[u][0]
#            print"temp3[0]", temp3[0]
            if(alpbt[v] == temp3[0]):
#                print"input and alpbt are same"
#                print "temp3[1]", temp3[1]
                freq_list.append(temp3[1])
#                print "freq_list", freq_list
#                input = input[1:]
#                length = length-1
#                print "length", length
                break
            else:
                u = u+1
                if(u == length):
                    freq_list.append(0)
        v = v+1
    return freq_list    


#Tests

print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]
