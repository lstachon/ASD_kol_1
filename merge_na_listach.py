class Node:
    def __init__(self, value = None):
        self.next = None
        self.val = value


class LinkedListA:
    def __init__(self):
        self.head = None

    def fixSort(self, node):
        temp = node
        new = Node()
        if(temp.next.next==None):
            if temp.val > temp.next.val:
                new.val = temp.next.val
                new.next = temp
                temp.next = None
                node = new
                return node
        else:
            if temp.val > temp.next.val:
                new.val = temp.val
                new.next = None
                temp= temp.next
                node=node.next
            else:
                prev = temp
                curr =temp.next
                next = temp.next.next
                a = 0

                while(next!=None and a==0):
                    if(prev.val<curr.val and curr.val<next.val):
                        prev=prev.next
                        curr = curr.next
                        next = next.next
                    else:
                        new.val = curr.val
                        new.next = None
                        prev.next = next
                        a=1
                if a == 0:
                    new.val = next.val
                    new.next = None
                    curr.next = None
                if new.val<temp.val:
                    new.next = temp
                    node = new
                prev = temp
                next = temp.next
                print("zajechuj")
                print(node.val)
                print(new.val)
                print(prev.val)
                print(next.val)
                while prev.val<new.val and new.val<next.val:
                    print("chuj")
                    prev = prev.next
                    next= next.next
                if prev.val<new.val and new.val<next.val:
                    prev.next = new
                    new.next = next
                if new.val > next.val:
                    next.next = new
        print(new.val)
        return node


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

    def srodeczek(self, l):
        if l is None:
            return l
        zlomek = l
        zygzak = l
        while zygzak.next != None and zygzak.next.next != None:
            zygzak = zygzak.next.next
            zlomek = zlomek.next
        return zlomek


    def merge(self, l, r):
        res = Node(-1)
        temp = res
        while l != None and r != None:
            if l.val <= r.val:
                new_node = Node()
                new_node.val = l.val
                temp.next = new_node
                temp = temp.next
                l = l.next
            else:
                new_node = Node()
                new_node.val = r.val
                temp.next = new_node
                temp = temp.next
                r = r.next
        while (l != None):
            new_node = Node()
            new_node.val = l.val
            temp.next = new_node
            temp = temp.next
            l = l.next
        while (r != None):
            new_node = Node()
            new_node.val = r.val
            temp.next = new_node
            temp = temp.next
            r = r.next
        return res.next


    def mergeSort(self, node):
        if node == None or node.next == None:
            return node
        mid = self.srodeczek(node)
        print('mid: ' + str(mid.val))
        # left = head
        right = mid.next

        mid.next = None
        left = self.mergeSort(node)
        right = self.mergeSort(right)
        print('left: ' + str(left.val))
        print('right: ' + str(right.val))

        total = self.merge(left, right)
        return total


# mrasnalista = None

list = LinkedListA()

# list.add_end(1)
# list.add_end(9)
# list.add_end(7)
# list.add_end(10)
# list.add_end(11)
# sorted_list = list.fixSort(list.head)
# list.print(sorted_list)
# list.print(list.head)
# sorted = list.mergeSort(list.head)
# print('sorted')
# list.print(sorted)
# mrasnalista = list.mergeSort(list.head)
# mrasnalista.print(mrasnalista)
# dualshot.add_end(dualshot, 1)
# dualshot.add_end(dualshot, 2)
# dualshot = dualshot.next
# mrasnalista = mrasnalista.next
# temp=merge(mrasnalista,dualshot)
# temp.print(temp)

def Partiton(A,low,high):
    i = low-1
    pivot = A[high]

    for j in range(low, high):
        if A[j]<pivot:
            i+=1
            A[j],A[i]=A[i],A[j]
    A[high],A[i+1] = A[i+1],A[high]
    return i+1

def quicksort(A,low,high):
    if(low<high):
        pi = Partiton(A,low,high)
        Partiton(A,pi+1,high)
        Partiton(A,low,pi-1)

A=[1,3,2,3,9,8]

quicksort(A,0,len(A)-1)

print(  )