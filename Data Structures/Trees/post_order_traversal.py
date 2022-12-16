def preorder(self, root_node):
    current = root_node
    
    if current is None:
        return

    self.preorder(current.left_child)
    self.preorder(current.right_child)
    
    print(current.data)