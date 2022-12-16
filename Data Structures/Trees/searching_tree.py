def search(self, data):
    
    current = self.root_node
    while True:
        if current is None:
            return None
        elif current.data is data:
            return data        
        elif current.data > data:
            current = current.left_child            
        else:
            current = current.right_child
            
tree = tree()
tree.insert(5)
tree.insert(2)
tree.insert(6)
tree.insert(7)
tree.insert(9)

for i in range(1, 10):
    found = tree.search(i)
    print("{}: {}".format(i, found))

