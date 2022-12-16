def insert(self, data):
    node = Node(data)
    
    if self.root_node is None:
        self.root_node = node
        
    else:
        current = self.root_node
        parent = None
        while True:
            parent = current
            
    if node.data < current.data:
        current = current.left_child
        
        if current is None:
            parent.left_child = node
            return
        
    else:
        current = current.right_child
        if current is None:
            parent.right_child = node
            return