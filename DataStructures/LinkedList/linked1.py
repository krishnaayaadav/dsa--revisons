


class Node:

    def __init__(self, data): 
        self.data  = data # node data here
        self.nexts = None # ref of next node here
    
    
    def __str__(self): # 
        return f'[{self.data}, {self.nexts}]'

class LinkedList: 

    def __init__(self):
        self.head = None

    def linkedLinkTranversal(self):

        head = self.head
        
        if not head:
            print('Your linked is empty')
            pass
        
        else: # thats means linked contains node or say having some data into it

            while head is not None:
                node  = head
                print(node.data)
                head  = node.nexts
    
    def largetAndSmallest(self):
        largest = 0
        smallest = 0
        head = self.head

        if not head:
            largest
        else:
            # updating smallest with first node of value
            smallest = self.head.data 

            while head is not None:
                # checking largest
                if (head.data > largest):
                    largest = head.data

                if head.data < smallest:
                    smallest = head.data
                head = head.nexts
        return {'largest': largest, 'smallest': smallest}
    
    def __str__(self):
        return f'{self.head}'


stuIds = [1,2,3,4,5,6,7,8,9,10]


n = Node(data=23)     # node obj

lList = LinkedList()  # linkedlist obj

lList.head = n  # putting node into head

def addNodes(preNode):
    previousNode = preNode

    for num in range(1,11):
        newNode = Node(num*2)
        previousNode.nexts = newNode
        previousNode = newNode

addNodes(preNode=n)

# lList.linkedLinkTranversal()
result= lList.largetAndSmallest()
print(result)