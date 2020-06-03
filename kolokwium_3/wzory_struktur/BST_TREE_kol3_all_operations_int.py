
class BSTNode:
    def __init__(self):
        self.key = None
        self.value = None
        self.parent = None
        self.left = None
        self.right = None

class BSTDict:
    def __init__(self, root=None):
        self.tree = root  # tu powinien być korzeń drzewa

    def find(self,key):
        r = self.tree
        while r is not None:
            if key > r.key:
                r=r.right
            if key <r.key:
                r=r.left
            if r.key == key:
                return r

    def insert(self,key,value):
        if self.tree.key is None and self.tree.value is None:
            self.tree.key = key
            self.tree.value=value
            return self.tree

        n = BSTNode()
        n.key=key
        n.value=value
        x = self.tree
        y = None
        while (x != None):
            y = x
            if (key < x.key):
                x = x.left
            else:
                x = x.right

        if (key < y.key):
            y.left = n
        else:
            y.right = n

        n.parent = y
        return y

    def succ(self,key):
        r = self.find(key)
        if self.max(self.tree.key).value == r.value:
            return None

        if r.right is None:
            x = r
            r = r.parent
            while r.right is x:
                r= r.parent
                x = x.parent
            return r

        r = r.right
        while(r.left!=None):
            r=r.left
        return r

    def pred(self,key):
        r = self.find(key)
        if self.min(self.tree.value).value == r.value:
            return None
        if r.left is None:
            x = r
            r = r.parent
            while r.left is x:
                r = r.parent
                x = x.parent
            return r

        r = r.left
        while r.right is not None:
            r = r.right
        return r

    def min(self,key):
        r = self.find(key)
        while r.left is not None:
            r=r.left
        return r

    def max(self,key):
        r = self.find(key)
        while r.right is not None:
            r = r.right
        return r

    def compare(self, key1, key2):
        if type(key1) == str:
            return comparing_strings(key1, key2)
        else:
            return compare_numbers(key1, key2)

    def remove(self, key):
        elem = self.tree
        if elem.right is None and elem.left is None and elem.parent is None:
            self.value= None
            self.key = None
            return None
        # jesli jest usuwany korzen
        if elem.key == key and elem.left is None:
            temp = self.min(elem.right)
            elem.key = temp.key
            elem.value = temp.value
            self.tree = temp
            elem.right = self.delete(temp.key, elem.right)
            return
        if elem.key == key and elem.right is None:
            temp = self.max(elem.left)
            elem.key = temp.key
            elem.value = temp.value
            self.tree = temp
            elem.right = self.delete(temp.key, elem.right)
            return
        self.delete(key, elem)

    def delete(self, key, node):
        if node is None:
            return node
        else:
            if self.compare(node.key, key) == -1:
                node.left = self.delete(key, node.left)
            elif self.compare(node.key, key) == 1:
                node.right = self.delete(key, node.right)
            else:
                if node.left is None:
                    temp = node.right
                    node = None
                    return temp
                elif node.right is None:
                    temp = node.left
                    node = None
                    return temp

                temp = self.min(node.right.key)
                node.key = temp.key
                node.value = temp.value
                node.right = self.delete(temp.key, node.right)
        return node


def compare_numbers(key1, key2):
    if key1 < key2:
        return 1
    elif key1 > key2:
        return -1
    else:
        return 0

def comparing_strings(a, b):
    for i in range(0, min(len(a), len(b))):
        if a[i] > b[i]:
            return -1
        elif a[i] < b[i]:
            return 1

    if len(a) > len(b):
        return -1
    elif len(a) < len(b):
        return 1
    elif len(a) == len(b):
        return 0


def check_if_balanced(r):
    if r is None:
        return True

def wraper_count_interval(r,a,b,count):
    if r is None:
        return 0
    if r.value >=a and r.value <=b:
        count = wraper_count_interval(r.right,a,b,count) + 1 + wraper_count_interval(r.left,a,b,count)
    elif r.value<a:
        wraper_count_interval(r.right,a,b,count)
    elif r.value>b:
        wraper_count_interval(r.left,a,b,count)
    return count

def count_interval(r,a,b):
    count =0
    return wraper_count_interval(r,a,b,count)


def check_if_bstwraper(node, down_size, upper_size):
    if node is None:
        return True

    if node.key<down_size or upper_size<node.key:
        return False

    return (check_if_bstwraper(node.left,down_size,node.key-1) and check_if_bstwraper(node.right,node.key+1,upper_size))

def check_if_bst(node):
    return check_if_bstwraper(node,-999999,999999)

def printT(r):
    r = r.tree
    table = prepare_to_print(r, [], 0)

    l = len(table)
    for i in table:
        if len(i) > 0:
            print(i)

def prepare_to_print(root, t, index):
    if root:
        if len(t) >= index:
            t.append([])
            t[index].append(root.value)
        else:
            t[index].append(root.value)
        index = index + 1
        prepare_to_print(root.left, t, index)
        prepare_to_print(root.right, t, index)
    return t


root = BSTNode()

r = BSTDict(root)

r.insert(4,4)
r.insert(1,1)
r.insert(7,7)
r.insert(0,0)
r.insert(2,2)
r.insert(6,6)
r.insert(9,9)
#
# print(check_if_bst(r.tree))
#
r.remove(1)
printT(r)
#
# print(r.succ(2).value)

print(count_interval(r.tree,0,7))

