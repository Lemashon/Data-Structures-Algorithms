class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        
#Append operation

    def append(self, data):
        
        #Encapsulate the data in a Node
        Node = node(data)
        
        if self.tail == None:
            self.tail = Node
        else:
            current = self.tail
                        
            while current.next:
                current = current.next
            current.next = node
            
words = SinglyLinkedList()
words.append("egg")
words.append("ham")
words.append("spam")