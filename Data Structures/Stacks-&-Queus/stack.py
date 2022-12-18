class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

        
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        
#Push operation

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        else:
            self.top = node
        self.size += 1
        
#Pop operation
    def pop(self):
        if self.top:
            data = self.top.data
                
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            
            else:
                self.top = None
            return data
        else:
            return None