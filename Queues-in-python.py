from typing import Deque


#Queue using Python Deque
#Python has an inbuilt feature of queue

from collections import deque
my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())
