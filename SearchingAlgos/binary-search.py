

arr = [1,2,3,4,5,5,6,7,8,8,9,9,10,11,121]

import random

"""
 Binary Search
 Approach: 
 Note: 
   Given sequnce must be sorted!
 
   1. Find mid of the given sequence or array
      formula: mid = start + (end - st)//2
   
   2. Compare arr[mid] with key
    if arr[mid] == key return the index

   3. If not than decide the portion 
        if(arr[mid] > key) :       if mead is greater then key than go left portion
        otherwise go the right portion

   4. update mid and repeat the same steps while start <= end

   5. If all iteration are done and key still not matched that it does not exist 
            in the given sequence then return -1 as not found
"""

class BinarySearch:
    # constructor 
    def __init__(self, arr, key):
        self.arr = arr
        self.key = key
    # binary-search implementation
    def binary_search(self):

        st = 0               # starting index
        end = len(self.arr)  # ending   index
        mid = st + (end - st)//2  # mid of arr

        while st <= end: # while start <= end: less than or equal to end

            if(arr[mid] ==self.key): # if arr[mid] is equal to key 
                return mid           # return index
            
            elif(arr[mid] > self.key): # if arr[mid] is greater than key
                end = mid -1

            else:
                st = mid + 1
            
            mid = st + (end - st)//2 # updating mid here
        return -1
    
b1 = BinarySearch(arr=arr, key=random.choice(arr))

result = b1.binary_search()
print(result)



