
# Remove nth node of linked list from last

class Node:

    def __init__(self, data):
        self.data  = data
        self.next  = None

class LinkedList:

    def __init__(self):
        self.head = None

n1 = Node(20)

linkeList = LinkedList()
linkeList.head = n1

n2 = Node(30)
n3 = Node(40)
n4 = Node(90)
n5 = Node(100)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


def remove_nth_node(head, n):

    if not head:
        return {
            'is_removed': False,
                 "count": 1
                 }
    
    data = remove_nth_node(head=head.next, n=n)
    is_remove = data['is_removed']
    count     = data['count']

    if not is_remove:
        if(count  == n+1):
            if head.next.next is None:
                head.next = None
                data['is_removed'] = True
            else:
                if head.next.next.next:
                    head.next = head.next.next
                    data['is_removed'] = True


        
        data['count'] += 1


    # print(data, type(data))
    return data

remove_nth_node(head=linkeList.head, n=2)



def traversal(head):

    if not head:
        return 
    
    traversal(head=head.next)
    print(head.data)

traversal(head=linkeList.head)

