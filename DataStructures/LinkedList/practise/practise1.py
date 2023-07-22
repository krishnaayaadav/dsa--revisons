
# Node
class Node:
    def __init__(self, data):
        self.data = data  # data initialization
        self.next = None
    
    def __str__(self):
        return f'[{self.data}, {self.next}]'

class LinkedList:

    def __init__(self):
        self.head = None # initial head is none
    
    def __str__(self):
        return f'{self.head}'
    

n1 = Node(10)

prev  = n1
for i in range(1, 11):
    newNode = Node(i*2) # new node obj
    prev.next = newNode
    prev      = newNode


linked_list = LinkedList() # always contains the first node the 

linked_list.head = n1
# Q1 Insert node at given position Nth position

def insertion_at_Nth_position(head , pos:int):

    if not head:
        return
    
    else:
        i = 0

        while head is not None:
            print(i,'data: ',  head.data)
            i += 1

            head = head.next


    


insertion_at_Nth_position(head=linked_list.head, pos=1)