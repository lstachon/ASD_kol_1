
from queue import PriorityQueue
q = PriorityQueue()
q.put(3)
q.put(2)
q.put(1)
while not q.empty():
    next_item = q.get()
    print(next_item)


