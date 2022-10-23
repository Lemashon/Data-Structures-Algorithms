class Node:
    #An object for storing a node of a linked list
    #Models two attributes and the link for the next node
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return "<Node data: %s>" % self.data
   
    