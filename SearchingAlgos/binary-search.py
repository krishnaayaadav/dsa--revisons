

arr = [1,2,3,4,5,5,6,7,8,8,9,9,10,11,121]

import random

"""
 Binary Search
 Approach: 

 Note: 
   Given sequnce must be sorted 
 
   1. Find mid of the given array
      mid = st + (end - st)//2
"""

class BinarySearch:

    def __init__(self, arr, key):
        self.arr = arr
        self.key = key
    
    def binary_search(self):

        st = 0               # starting index
        end = len(self.arr)  # ending   index
        mid = st + (end - st)//2  # mid of arr


        while st <= end:

            if(arr[mid] ==self.key): # if arr[mid] is equal to key 
                return mid           # return index
            
            elif(arr[mid] > self.key): # if arr[mid] is greater than key
                end = mid -1

            else:
                st = mid + 1
            
            mid = st + (end - st)//2 # finding mid here
        return -1
    
b1 = BinarySearch(arr=arr, key=random.choice(arr))

result = b1.binary_search()
print(result)



