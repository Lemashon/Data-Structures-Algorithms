def peek(self):
    if self.top:
        return self.top.data
    else:
        return None