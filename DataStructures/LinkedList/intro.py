# linked list basically are data-structure which store data non-contiguous location.
# In Each linked it contains node represents the element of linked list

# where each contains data and pointer which is pointing to next node

# Node
class Node:
    def __init__(self, dataval):
        self.dataval = dataval  # data initialization
        self.nextval = None
    
    def __str__(self):
        return f'[{self.dataval}, {self.nextval}]'

class LinkedList:

    def __init__(self):
        self.headval = None

# linked obj creation
mylist = LinkedList()
        
print(mylist.headval)

mylist.headval = Node(dataval=12)

print(mylist.headval)
