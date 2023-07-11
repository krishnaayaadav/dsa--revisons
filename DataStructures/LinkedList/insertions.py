

class Node:

    def __init__(self, data):
        self.data     = data
        self.nextNode = None

    
    def __str__(self):
        return f'[{self.data}, {self.nextNode}]'
    

class LinkedList:

    def __init__(self):
        self.head = None

    def traversal(self):
        """Approach: 
           We are first checking that if linked_list is not empty that means it have some into it.
           now we know that node contains two things data|ref_of_next_node as node [23,nextNode]
           So we running a while until head become none that means when linked_list become empty
           So we are first accessing the first node that containing some data and refrence of the next node
           node  = [120, nextNode]

           print(node.data)
           head = head.nextNode  # updating the head
        """
        
        head = self.head
        if not head:
            print('Linked is empty')
        
        else:
            while head is not None:
                data = head.data
                print(data)
                head = head.nextNode # here pointing to nextNode the updating the head
    
    def insertion_at_first_position(self,node):
        if not self.head: # empty linked list
            self.head = node
        else:
            node.nextNode = self.head
            self.head     = node
            # previousNode  = self.head # storing the previous node
            # self.head = node  # now pointing new node at first position
            # self.head.nextNode = previousNode # adding the existing node into the same linked list

    def insertion_at_last_position(self, node):

        if not self.head: # if it emplty
            self.head = node
        else:
            head = self.head

            while head is not None: # going till last node and then adding into it
                node = head
                # print(data)

                if not node.nextNode: # if head is none it means we at last position
                    print('Now add new node at last position')
                    head = node
                    # print(head.data)
                    break

                head = head.nextNode # updating head

    def insertion_at_given_position(self, pos:int, newNode):
        
        if  not self.head:
            print('Linked is emplty inserting at first position')
            self.head = newNode
        else:
            
            head = self.head
            prevPos = pos-1
            count = 1
            is_inserted = False

            while head is not None:
                # print(node.data, count)

                if (count == prevPos):
                    # print(node.data, 'yaha pe insert here')
                    newNode.nextNode = head.nextNode
                    head.nextNode = newNode
                    is_inserted = True
                    # print(head.data, 'yaha pe insert here')


                # if (currentPos == previousPos):
                #     newNode.nextNode = head.nextNode
                #     head.nextNode    = newNode
                #     is_inserted = True
                #     break
                count += 1

                head  = head.nextNode
            return f'Insertion status: {is_inserted} '

                

    def __str__(self):
        return f'{self.head}'

n1 = Node(81)
link_list = LinkedList()
link_list.head = n1

def add_multiple_nodes(num_of_nodes=10):
    prevNode = n1
    for num in range(1, num_of_nodes+1):
        newNode = Node(num)
        prevNode.nextNode = newNode
        prevNode = newNode

add_multiple_nodes(10) # that done

is_inserted = link_list.insertion_at_given_position(pos=31, newNode=Node(777))
# print(is_inserted)

link_list.traversal()
# print(n1)
# print(link_list)

# link_list.head = n1   # first node in linked list head
# n3 = Node(33)
# n1.nextNode = n3

# n4 = Node(44)
# n3.nextNode = n4 
# # print(link_list)


# # link_list.traversal()

# n5 = Node(555) 

# # print(n5.nextNode, n5)
# link_list.insertion_at_first_position(node=n5)

# # after insertion at first position of the node
# # link_list.traversal()

# # insertion at last position

# link_list.insertion_at_last_position(node=Node(77))

# # insert at 3 position
# n6 = Node(333)

# print(link_list.head)
# link_list.insertion_at_given_position(pos=3, newNode=n6)
# print('\n \n')
# link_list.traversal()