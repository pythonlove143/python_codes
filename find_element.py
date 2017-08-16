# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(list_name,value):
    index = 0
    for i in list_name:
        if(i == value):
            return index
        else:
            index = index + 1
            if(index == len(list_name)):
                return -1
        
#for i in list_name
#    if(index ==value):
#        return index
#    i = i + 1
#return -1


print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
