class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []
        
#Enqueue operation

    def enqueue(self, data):
        self.inbound_stack.append(data)
        
queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
print(queue.inbound_stack)

#Dequeue operation
