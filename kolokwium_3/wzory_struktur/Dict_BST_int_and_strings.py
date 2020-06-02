#Lukasz Stachon
#algorytm działa dla kluczy liczbowych oraz kluczy w formie napisu
class BSTNode:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value


class BSTDict:
    def __init__(self, root =None):
        self.tree = root  # tu powinien być korzeń drzewa

    # dodaje element do drzewa
    def insert(self, key, value):
        # drzewo jest puste
        if self.tree is None:
            node = BSTNode(key, value)
            self.tree = node
        else:
            temp = self.tree
            self.add(temp, key, value)

    # gdzie sie nznajduje, key -dodawany/szukany
    def add(self, r, key, val):
        if self.compare(r.key, key) == 0:
            # podmien wartosc
            r.value = val
            return
        if self.compare(r.key, key) == 1:
            if r.right is None:
                new_node = BSTNode(key, val)
                r.right = new_node
                return
            else:
                self.add(r.right, key, val)
        else:
            if r.left is None:
                new_node = BSTNode(key, val)
                r.left = new_node
                return
            else:
                self.add(r.left, key, val)

    def find(self, r, key):
        if r.key == key:
            return r
        if self.compare(r.key, key) == 1:
            if r.right is None:
                return None
            self.find(r.right, key)
        else:
            if r.left is None:
                return None
            self.find(r.left, key)

    # znajduje najmnijeszy element w poddrzewie
    def min(self, n):
        while n.left is not None:
            n = n.left
        return n

    # znajduje najwiekszy element w poddrzewie
    def max(self, n):
        while n.right is not None:
            n = n.right
        return n

    def compare(self, key1, key2):
        if type(key1) == str:
            return comparing_strings(key1, key2)
        else:
            return compare_numbers(key1, key2)

    def remove(self, key):
        elem = self.tree
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

                temp = self.min(node.right)
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

def printT(r):

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

r = BSTNode('d','d')
table = BSTDict(r)
table.insert('b','b')
table.insert('f','f')
table.insert('a','a')
table.insert('c','c')
table.insert('e','e')
table.insert('g','g')

printT(r)

table.remove('d')

printT(r)



