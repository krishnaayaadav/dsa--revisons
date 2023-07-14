"""
Count frequency of each element in the array

Example 1:
Input: arr[] = {10,5,10,15,10,5};
Output: 10  3
	    5  2
        15  1
Explanation: 10 occurs 3 times in the array
	         5 occurs 2 times in the array
            15 occurs 1 time in the array
"""
class FrequencyCounter:

    def __init__(self, arr:tuple):
        self.arr = arr
        self.is_hashed = False
        self.hashed_data = None
        self.store_hashed_data() # calling hashing method
    
    def make_hashed_table(self):
        unique_data  = {}
        # converting into sets
        temp_arr = tuple(set(self.arr)) # elm

        # print(len(temp_arr) , len(self.arr))

        for i in range(0, len(temp_arr)):
            current_elm = temp_arr[i]
            unique_data[current_elm] = self.arr.count(current_elm)
        
        
        return unique_data
    
    def store_hashed_data(self):
        hashed_data = self.make_hashed_table()
        if not hashed_data:
            pass
        else:
            self.is_hashed = True
            self.hashed_data = hashed_data
    
    def make_queries(self, *args):
        query_result = {}
        for i in range(0, len(args)):
            
            query = args[i]
            try:
                count = self.hashed_data[query] # fetching the coutn
            except:
                count = 0
            finally:
                query_result[query] = count
        
        return query_result
            # print(query)
        
my_arr = list(range(1,11)) + list(range(1,11)) + list(range(1,11)) + list(range(1,11)) +list(range(1,11))
f = FrequencyCounter(arr=my_arr)


result = f.make_queries(12,21,2,2,45,54,5)

print(result)

def count_occurent_without_built_function(arr:tuple):
    pass