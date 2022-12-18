class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0
#Enqueu operation

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1
        
#Dequeu operation
    def dequeu(self):
        data = self.items.pop()
        self.size -= 1
        return data