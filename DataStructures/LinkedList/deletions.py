
# deletion in linked list

from insertions import Node, LinkedList

# we using inheritance here

class LinkedList(LinkedList):

    def __init__(self):
        self.head = None # initilize empty linked list

    def delete_first_node(self):
        """Deletion of the first node of empty or existing linked"""

        if not self.head:
            print('Linked is empty')
        else:
            node = self.head # data
            # now head is pointing the next node
            self.head = node.nextNode
    
    def delete_last_node(self):
        """Last node deletion here"""

        if not self.head:
            print('linked list is empty of delete')
        else:
            head = self.head

            while head is not None:
                node = head # getting here node we know one in head their some node is ther node[data|nextNode]
                # print(node.data)
                head = node.nextNode # updating the head

                lastNode = node.nextNode # finding next node 
                if lastNode.nextNode == None:  # checking is it last node
                    node.nextNode = None
                    
                    break

    def delete_specific_node(self, nodePos: int):

        if not self.head:
            print('Linked list is empty')
        else:
            head  = self.head # node[data|nextNode]
            prevNode = None
            nextNodes = None

            while head is not None:
                print(head.data)
                prevNode = head
                nextNodes = head.nextNode

                head = head.nextNode # updating head
            
    #  [data|nextNode] >> [data|nextNode] >> [data|nextNode]
    
linked_list = LinkedList()

n1 = Node(77)
n2 = Node(88)
n3 = Node(999)

# pointing the first node
linked_list.head = n1 # node=data|nextNode
n1.nextNode = n2
n2.nextNode = n3 

n3.nextNode = Node(1000)

# linked_list.delete_first_node()

# linked_list.delete_last_node()

# linked_list.traversal()

# Now we going perform deletion at beggining, last and at specific given position.

# delete first Node in linked list


linked_list.delete_specific_node(nodePos=2)