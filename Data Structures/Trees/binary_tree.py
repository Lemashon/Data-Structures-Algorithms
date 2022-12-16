class Node:
    
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None
        
#Create nodes
        
n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")

#Connect the nodes with each other

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4

#Traverse the tree structure

current = n1
while current:
    print(current.data)
    current = current.left_child