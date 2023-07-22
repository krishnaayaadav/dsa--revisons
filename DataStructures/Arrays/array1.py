
from array import array


stu_ids = array('i', [1,2,3,4,5])

# largest elements

i = 0 

while i<len(stu_ids):
    print(stu_ids[i])
    i += 1

def find_largest(arr):
    largest = arr[0] # i assuming array of first element is largest
    
    i = 0
    while i<len(arr):
        elm = arr[i]

        if(elm > largest): # if it is greatest than largest agar ye largest se bhi largest to update larges

            largest = elm  
    
    return