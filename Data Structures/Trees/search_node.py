def get_node_with_parent(self,data):
    parent = None
    current = self.root_node
    if current is None:
        return (parent, None)
    
    while True:
        if current.data == data:
            return(parent,current)
        
        elif current.data > data:
            parent = current
            current = current.left_child
            
        else:
            parent = current
            current = current.right_child
            
    return (parent,current)