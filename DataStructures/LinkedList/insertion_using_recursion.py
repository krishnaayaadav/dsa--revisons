# Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None
    

    def __str__(self):
        return f'[{self.data}, {self.nextNode}]'
   
# linked list class
class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        return f'{self.head}'


def traverse_linked_list_using_recusrsion(head):

    if not head: 
        return
    # calling the same function with different next node
    traverse_linked_list_using_recusrsion(head=head.nextNode)
    print(head.data)

    
linked_list = LinkedList()
n1 = Node(10)
linked_list.head = n1

# create some new node using loops
prevNode = n1
for i in  range(1, 11):
    newNode = Node(i*2)
    prevNode.nextNode = newNode
    prevNode = newNode



# traverse_linked_list_using_recusrsion(head=n1)



def insertion_at_first(linkList, newNode):
    if not linkList.head:
        linkList.head = newNode
    else:
        newNode.nextNode = linkList.head
        linked_list.head = newNode
        

def insertion_at_last_recursion(head, newNode):
    if not head:
        return
    
    insertion_at_last_recursion(newNode=newNode, head=head.nextNode)
    
    # insertion at last node
    if not head.nextNode: # [12,None] if node.nextNode = None
        head.nextNode = newNode



l1 = LinkedList()
newNode = Node(777)

insertion_at_first(linkList=linked_list, newNode=newNode)


print(linked_list.head)

# insertion_at_last_recursion(head=linked_list.head, newNode=Node(2000))
# print(linked_list)

def deletion_at_last_recursion(head):

    if not head:
        return 1
    
    # calling the same function via passing head.nextNode changing nodes
    result_no = deletion_at_last_recursion(head=head.nextNode)

    if(result_no == 2):
        if (head.nextNode):
            if not head.nextNode.nextNode:
                head.nextNode = None
    
    return result_no + 1


    

deletion_at_last_recursion(head=linked_list.head)

print(linked_list.head)
