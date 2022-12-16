#Finding the minimum and maximum nodes

def find_min(self):
    current = self.root_node
    while current.left_child:
        current = current.left_child
    return current