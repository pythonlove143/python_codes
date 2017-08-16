# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    i = 0
    x = 0
    a = 0
    temp1 = []
    temp2 = []
    length = len(string)
    string = string[::-1]
#    print string
    number = int(string)
#    print number 
    while(i<length):
        a = number%10
        number = number/10
#        print "a",a
#        print "number",number
        if (temp1 == []):
            temp1.append(a)
        else:
            x = temp1[len(temp1)-1]
            if (x >= a):
                temp2.append(a)
#                print "temp2", temp2
            else:
                if (temp2 != []):
                    temp1.append(temp2)
                    temp2 = []
                temp1.append(a)
#               print "temp1", temp1
            if (number ==0 and temp2 != []):
                temp1.append(temp2)
#                print "temp1", temp1
        i = i+1
                
    return temp1         
        
        
        
        
    # YOUR CODE

#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result
