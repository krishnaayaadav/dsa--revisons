
class HashTable:

    def __init__(self, size):
        self.size = size
        # generating blnk array or list
        self.table = [ [] for _ in range(self.size)]

    def hash_function(self, key):
        """has function will generate unique index/key"""
        return hash(key) % self.size
    
    def set(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

   

# h = HashTable(size=10)

# print(h.table)
# h.set(key=4, value=4000)
# print(h.table)

arr = [1,2,3,4,5,6,7,1,8,9,10]

# stuData = {}
# for i in range(0, len(arr)):
#     print(stuData)
#     id = arr[i]
#     stuData[id] = {'value': id, 'occurenece': arr.count(id)}

def find_occurenece_of_num(arr, *queries):
    stuData = {}
    for i in range(0, len(arr)):
        # print(stuData)
        id = arr[i]
        stuData[id] = {'value': id, 'occurenece': arr.count(id)}

    # making queries
    query_output = []

    for i in range(0, len(set(queries))):
        q1 = queries[i]
        if(q1 in stuData.keys()  ):
            query_output.append(stuData[q1])

    return query_output

result = find_occurenece_of_num(arr, 4,5,78,98,5,12,20)
print(result)

