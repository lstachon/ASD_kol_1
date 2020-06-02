class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        self.parent = None
        self.index = []


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
            t[index].append((root.value))
        else:
            t[index].append(root.value)
        index = index + 1
        prepare_to_print(root.left, t, index)
        prepare_to_print(root.right, t, index)
    return t


# def sum(root):
#     if (root != None):
#         if root.value is None:
#
#             if root.left is not None and root.right is not None and root.left.value!= None and root.right.value!= None:
#                 root.value = root.left.value+ root.right.value
#
#                 return sum(root.parent)
#             if root.left == None and root.right != None and root.right.value != None:
#                 root.value = root.right.value
#                 return sum(root.parent)
#             if root.left != None and root.right == None and root.left.value != None:
#                 root.value = root.left.value
#                 return sum(root.parent)
#             if root.left != None and root.left.value is None:
#
#                 sum(root.left)
#             if root.right != None and root.right.value is None:
#
#                 sum(root.right)

class IntervalSums:

    def __init__(self, n):
        self.table = [0]*n
        self.root = Node()
        self.create_tree(0, n - 1, self.root)

    # if r.i =



        return y

    def interval(self, i, j):
        return

    def sum(self, root):
        if (root != None):
            if root.value is None:

                if root.left is not None and root.right is not None and root.left.value != None and root.right.value != None:
                    root.value = root.left.value + root.right.value

                    return sum(root.parent)
                if root.left == None and root.right != None and root.right.value != None:
                    root.value = root.right.value
                    return sum(root.parent)
                if root.left != None and root.right == None and root.left.value != None:
                    root.value = root.left.value
                    return sum(root.parent)
                if root.left != None and root.left.value is None:
                    sum(root.left)
                if root.right != None and root.right.value is None:
                    sum(root.right)


    def create_tree(self, a, b, r):
        if a == b:
            x = Node()
            x.value = self.table[a]
            x.parent = r
            r.left = x
            r.value = x.value
            r.index.append(a)
            return

        if a + 1 == b:
            x = Node()
            x.value = self.table[a]
            y = Node()
            y.value = self.table[b]
            x.parent = r
            y.parent = r
            r.left = x
            r.right = y
            r.value = x.value + y.value
            x.index.append(a)
            y.index.append(b)
            return

        r.left = Node()
        r.left.parent = r

        r.right = Node()
        r.right.parent = r

        c = a + ((b - a) // 2)
        self.create_tree(a, c, r.left)
        self.create_tree(c + 1, b, r.right)


IS = IntervalSums(4) # tworzy tablicę [0,0,0,0]
IS.set(0, 10) # [10,0,0,0]
IS.set(2, -2) # [10,0,-2,0]
IS.set(3, 1) # [10,0,-2,1]

IS.interval(0,3) # zwraca 10+0+(-2)+1 = 9
IS.interval(1,2)

tab = [1, 7, 2, 3, 6, 1]
a = 0
b = len(tab) - 1
root = Node()
create_tree(tab, a, b, root)
printT(root)

# # tworzy tablcę rozmiaru n, zainicjowaną zerami
# def set( self, i, val ):
# # zmienia zawartosc tablicy pod indeksem i na val
# def interval( self, i, j ):
# # zwraca sumę elementów tablice na pozycjach od i do j wlacznie
# Przykładowe użycie klasy:
# IS = IntervalSums(4) # tworzy tablicę [0,0,0,0]
# IS.set(0,10) # [10,0,0,0]
# IS.set(2,-2) # [10,0,-2,0]
# IS.set(3,1) # [10,0,-2,1]
# IS.interval(0,3) # zwraca 10+0+(-2)+1 = 9
# IS.interval(1,2) # zwraca 0-2 = -2
