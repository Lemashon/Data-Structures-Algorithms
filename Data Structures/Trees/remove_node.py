def remove(self, data):
    parent, node = self.get_node_with_parent(data)
    
    if parent is None and node is None:
        return False
    
    #Get children count
    
    children_count = 0
    
    if node.left_child and node.right_child:
        children_count = 2
        
    elif(node.left_child is None) and (node.right_child is None):
        children_count = 0
    
    else:
        children_count = 1
        
    #Handling the case where the node has no children
    
    if children_count == 0:
        if parent:
            if parent.left_child is node:
                parent.right_child = None              
            else:
                parent.left_child = None
                
        else:
            self.root_node = None
            
    #Handling the case where the node has 1 children
    
    elif children_count == 1:
        next_node = None
        if node.left_child:
            next_node = node.left_child
            
        else:
            next_node = node.right_child
            
        if parent:
            if parent.left_child is node:
                parent.left_child = next_node
                
            else:
                parent.right_child = next_node
        else:
            self.root_node = next_node
            
    #Handling the case where the node has 2 children
    
    else:
        perent_of_leftmost_node = node
        leftmost_node = node.right_child
        while leftmost_node.left_child:
            parent_of_leftmost_node = leftmost_node
            leftmost_node = leftmost_node.left_child
            
            node.data = leftmost_node.data
            
        if parent_of_leftmost_node.left_child == leftmost_node:
            parent_of_leftmost_node.left_child = leftmost_node.right_child
            
        else:
            parent_of_leftmost_node.right_child = leftmost_node.right_child