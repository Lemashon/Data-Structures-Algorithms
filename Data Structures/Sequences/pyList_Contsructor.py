class pyList:
    def __init__(self, contents = [], size = 10)
    self.items = [None] * size
    self.numItems = 0
    self.size = size
    
    for e in contents:
        self.append(e)