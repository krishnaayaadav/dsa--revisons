
"""
 Searching:  is way checking weather some particular key/element is exist in given sequence(arr,list etc) or not.
 
 Approach: 
 Linearch Search
 1. We traverse our given sequence by one by one and compare the current element with key
 2. If key matched with the current than return that index
 3. Go in next do same thing untill we iterate all elements of the sequence
 4. If not found than return -1 that's  means key does not exists in the given sequence
 
"""
from array import array

class LinearSearch:
    #constructor here
    def __init__(self, arr, key):
        self.arr = arr  # sequence here array,list, tuple etc
        self.key = key  # key which we want to check
    
    # linear_search method here 
    def linear_search(self):

        i = 0
        index = -1            # assuming that key does not exist in our sequence 


        while i<len(self.arr):

            elm = self.arr[i]     # getting the current element

            if(elm == self.key):  # checking weather current value is equal to given key or not
                index = i         # updating the index if key is found in the sequence
                
                break
            i   += 1              # updating the value of i to go i next iteration
        return index
    
    def linear_search_using_recursion(self, arr, arr_len, key):

        if arr_len == 0:
            return {
                'index': arr_len,
                'found': False
            }
        
        data = self.linear_search_using_recursion(arr=self.arr, arr_len=arr_len-1, key=key)

        if not data['found']:
            if(arr[data['index']] == key):
                data['found'] = True
            else:
                data['index'] = arr_len

       
       
        return data 
        
my_arr = array('i', [1,34,45,56,56,6,778,45,56,67,77,8,34,45,56,7,67,34,23,111, 7778])
key    = 7778
l1 = LinearSearch(arr=my_arr, key=key)

index = l1.linear_search()
print(index)

result = l1.linear_search_using_recursion(arr=l1.arr, arr_len=len(l1.arr), key=key)
print(result['index'])