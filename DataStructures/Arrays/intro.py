
"""
  Arrays: are use to use store multiple elements into single variable having same data types in ordered format.
          It can homogenous data elements we can access them using indexing.
          Array may contains duplicate elements

          To create array in python we use to array module 
"""

from array  import array

# array creation
stu_ids = array('i', [1,2,4,5,5,6,4,5,5,63,2,1])

# add new element to existing array

stu_ids.append(12) # add element at end of array
stu_ids.append(34) # add new element at end of the array

# add new at specific position
stu_ids.insert(0, 77) # insert method is use insert the elements at given index 

print(stu_ids[0])

# delete elements from array
# remove, pop method are use delete the array elements

# remove is when array elements is given

val= 64

def remove_array_elm(arr, key):

    try:
        arr.remove(key) # those code which may some exception

    except:                 # how we going to handle exception
        print(f'given {key} does not exist in array')

    else:                   #if it normal flow
        print(f'given {key} is removed from  array')
    
# 15-20 
# remove_array_elm(arr=stu_ids, key=5)

result = None
try:
    result = stu_ids.pop(100) # will remove the given index value if it exist and return the value

except:
    pass

else:
    print(result, 'is remove successfully')

finally:
    print('Removal operation is done')
print(result)

# traversal of array

#using while loop
i = 0

while i< len(stu_ids):

    print(stu_ids[i], end=' ')

    i += 1

# traversal using recursion

def recursive_traversal(arr, arr_len):

    if(arr_len < 0):
        return 
    
    recursive_traversal(arr=arr, arr_len=arr_len-1)

    print(arr[arr_len], end=' ')

recursive_traversal(arr=stu_ids, arr_len=len(stu_ids) -1)

