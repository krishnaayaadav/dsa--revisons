

class Tree:

    def __init__(self, root_node=None):
       self.root = root_node

    def __str__(self):
        return f'{self.root}'

t = Tree() # obj of tree

class Node:

    def __init__(self, data):
        self.left  = None
        self.data  = data
        self.right = None

    
    def __str__(self):
        return f'[{self.left}, {self.data}, {self.right}]'

n1 = Node(10)

# print(n1)
print('before adding node: ', t)

t.root = n1

print('after adding node: ', t)
n2 = Node(20)
n1.left = n2

n2.left = Node(200)