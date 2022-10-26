#run each individual code separately
#create a new stack

my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(13)
my_stack.append(20)
print(my_stack)

print(my_stack.pop())
print(my_stack.pop())
print(my_stack)

#stack using a list with a wrapper Class
def stack():
    def __init__(self):
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
    def __Str__(self):
        return str(self.stack)
    
    #Test Code for Stack Wrapper class
    
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(3)
    print(my_stack)
    print(my_stack.pop())
    print(my_stack.peek())
    print(my_stack.pop())
    print(my_stack.pop())
    