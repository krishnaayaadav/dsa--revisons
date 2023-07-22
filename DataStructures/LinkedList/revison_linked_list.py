
# topic:  creation, traversal, insertion, deletion, updation, searching

# creation

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f'[{self.data}, {self.next}]'

class LinkedList:

    def __init__(self):
        self.head = None # it points the first the initially
    
    def __str__(self) -> str:
        return f'{self.head}'


linked_list = LinkedList() # obj 
node1  =     Node(100)

# linked_list.head # it None currently

linked_list.head = node1 # now head it pointing the first node of linked list


# 
def node_creator(lastNode):

    for i in range(1, 11):
        newNode = Node(i*2)
        lastNode.next = newNode
        lastNode = newNode
    
node_creator(lastNode=node1)

def traverse_linked(head):

    if not head:
        return
    
    # we know head point some node and nodes have two things data|nextNode
    print('\n')
    while head is not None:
        print(head.data)
        
        #updating the head to point the next using next pointer
        head = head.next

# traverse_linked(linked_list.head)

########## Insertion in Linked List #####

### At first position

# there will be two situation either the linked is empty or it may contains some existing nodes

# 
"""
   if it empty
   Approach: 

   If linked list is empty
   then we store or  point the head to newNode
   head = newNode[data|nextNode]

   If not empty:

   Approach: 

   Then we first check is linked is not None if true

   we store firstNode in newNode.next me
   then after that we point the newNode linkedList head me


"""

def insertion_at_first_position(head, newNode):

    if head is None: # means if linked list is empty
        head = newNode 
         
    else:
        # otherwise linked contains some existing nodes than
        # currenlty head is pointing some node here
        newNode.next = head  # so we are link exsiting node with newNode

        head  = newNode      # updating the head with newNode without any data loss
    return head
    
    # traverse_linked(head=head)

# linked_list.head =  insertion_at_first_position(head=linked_list.head, newNode=Node(777))

# traverse_linked(head=linked_list.head)

###### Insertion At Last 
"""
  Insertion at last 
  
  1.  We will check if head.next == None that means it is a  last node
  2.  Then we insert our newNode at that position
  3.  break loop

"""

# traverse_linked(head=linked_list.head)

def insertion_at_last(head, newNode):

    if not head:
        print('\n Linked is empty')
        head  = newNode
    # not empty

    while head is not  None:

        if head.next == None: # checking the last node
            head.next = newNode
            break
        
        head = head.next

# insertion_at_last(head=linked_list.head, newNode=Node(7777))

# traverse_linked(linked_list.head)

## insertion at last using recursion

def insertion_last_by_recursion(head, newNode=Node(888)):

    if not head: # meas head is None
        return  0  # return back
    
    insertion_last_by_recursion(head=head.next, newNode=newNode)

    if head.next == None: # if it last node
        head.next = newNode # then add newNode into it
    
insertion_last_by_recursion(head=linked_list.head, newNode=Node(78887))
    

##### Insertion at given position

# using recursion

"""
   [10 | next]  [45 | next]   [100 | next]   [78 | next]   [65 | next]  
      
      pos1          pos2          pos3          pos4          pos5

   
   Insert at position 3
"""

def insertion_at_Nth_node(head, pos:int, newNode=Node(5550)):

    if pos == 1 and not head:
        head = newNode
        return
    
    # that mens pos may equal to one or greater than that
    firstNode = head
    counter = 0

    while head is not None:
        counter +=1

        if(counter  == pos - 1): #0 + 1 = 1
            if(head.next):
                newNode.next = head.next
                head.next    = newNode
                break

        head  = head.next

# traverse_linked(linked_list.head)

# head = insertion_at_Nth_node(head=linked_list.head, pos=3)


head = linked_list.head

# traverse_linked(head)

def insertion_Nth_position(head,  pos:int, newNode=Node(1001)):

    # pos 1

    if not head and pos ==1: # linked is empty
        head = newNode
        return # return back
    
    counter = 1
    while head is not None:

        if pos == 1:
            newNode.next = head
            head = newNode
            return head
        else:
            if counter + 1 == pos:
                if head.next:
                    newNode.next = head.next
                    head.next    = newNode
                    break
                else:
                    head.next = newNode
                    break
        
        counter += 1
        
        head = head.next # updating our head

myhead = insertion_Nth_position(head=head, pos=13)
if  myhead:
    head = myhead



##### Deletion of linked list


def deletion_at_given(head, pos):

    if not head: # if linked list is empty
        return # return back
    
    count = 1

    while head is not None:

        if (pos == 1):
            if(head.next): # if head.next is containing some next node  than point the next node here
                head = head.next
                return head
        
        if (count + 1 == pos): # 1+1 == 2:true
            if (head.next.next):
                head.next = head.next.next
                break
            else:
                head.next = None
                break
        
        count += 1
        
        head = head.next
traverse_linked(head)

myhead = deletion_at_given(head=head, pos=13)
if myhead:
    head = myhead

traverse_linked(head)
