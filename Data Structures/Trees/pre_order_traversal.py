def preorder(self, root_node):
    current = root_node
    
    if current is None:
        return
    print(current.data)
    self.preorder(current.left_child)
    self.preorder(current.right_child)