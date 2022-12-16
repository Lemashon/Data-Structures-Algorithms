#recursive function

def inorder(self, root_node):
    current = root_node    
    if current is None:
        return
    
    self.inorder(current.left_child)
    print(current.data)
    self.inorder(current.right_child)
    