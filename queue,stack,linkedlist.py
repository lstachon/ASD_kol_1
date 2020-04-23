class Node:
    def __init__(self, value = None):
        self.next = None
        self.val = value

class LinkedListA:
    def __init__(self):
        self.head = None

        def print(self, node):
            head_tmp = node
            while (head_tmp != None):
                print(head_tmp.val)
                head_tmp = head_tmp.next

        def add_end(self, x):

            if self.head == None:
                new = Node()
                new.val = x
                new.next = None
                self.head = new
            else:

                temp = self.head
                while (temp.next != None):
                    temp = temp.next

                new = Node()
                new.val = x
                new.next = None
                temp.next = new




###############################################
# stack

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
# print(stack)
a = stack.pop()
# print(a)
# print(stack)

###############################################
# queue

queue=[]
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.pop(0)
print(queue)
