# wezel drzewa BST
class BSTNode:
    def __init__(self, key, value):
        self.left = None
        self.right = None
    # pola parent nie ma -- nie jest w tym zadaniu potrzebne
        self.key = key
        self.value = value

class BSTDict:
    def __init__( self ):
        self.tree = None # tu powinien być korzeń drzewa

    def insert(self, key, value):
        # drzewo jest puste
        if self.tree is None:
            node = BSTNode(key, value)
            self.tree = node
        else:
            self.s(self.tree, key, value)


    def compare(self, key1, key2):
        if key1 < key2:
            return 1
        elif key1 > key2:
            return -1
        else:
            return 0

    # gdzie sie nznajduje, key -dodawany/szukany
    def s(self, r, key, val):
        if self.compare(r.key, key) == 0:
            #podmien:
            r.val = val
            return
        if self.compare(r.key, key) == 1:
            if r.right is None:
                new_node = BSTNode(key, val)
                r.right = new_node
                return
            else:
                self.s(r.right, key,val)
        else:
            if r.left is None:
                new_node = BSTNode(key, val)
                r.left = new_node
                return
            else:
                self.s(r.left, key, val)

    #def remove( self, key ):

def comparing_number(a,b):
    if a > b:
        return 1
    elif a>b:
        return -1
    elif a == b:
        return 0

def comparing_strings(a,b):
    for i in range(0,min(len(a),len(b))):
        if a[i] > b[i]:
            return 1
        elif a[i] < b[i]:
            return -1

    if len(a)>len(b):
        return 1
    elif len(a)<len(b):
        return -1
    elif len(a)==len(b):
        return 0

def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val)
        print_tree(root.right)

# usuń z drzewa węzeł z kluczem key


def find(root, element):
    while root is not None:
        if root.val is element:
            return root.val
        elif root.val<element:
            root = root.right
        else:
            root = root.left
    return None



# #################################
# def printT(table):
#     l = len(table)
#     for i in table:
#         if len(i) > 0:
#             print(i)
#
# def prepare_to_print(root, t, index):
#     if root:
#         if len(t) >= index:
#             t.append([])
#             t[index].append(root.val)
#         else:
#             t[index].append(root.val)
#         index = index + 1
#         prepare_to_print(root.left, t, index)
#         prepare_to_print(root.right, t, index)
#     return t

def print_tree(root, s):
    if root:
        print(s + str(root.val))
        print_tree(root.left,  ' ' + s)
        print_tree(root.right, s + ' ')

bstdict = BSTDict()

bstdict.insert(10,"siusiak")
bstdict.insert(11,"ciapek")
bstdict.insert(9,"czucza")

print_tree()
