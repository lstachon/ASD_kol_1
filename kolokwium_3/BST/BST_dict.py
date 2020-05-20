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


    def insert( self, key, value ):
        return

    def remove( self, key ):
        return




def print_tree(root):
    if root:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)

def printT(table):
    for i in table:
        print(i)

def prepare_to_print(root, t, index):
    if len(t) < index:
        t[index] = root.val
    else:
        t[index].append(root.val)
    prepare_to_print(root.left, t, index + 1)
    prepare_to_print(root.right, t, index + 1)

a = [[0], [1,2], [1,2,3,4]]

printT(a)

# usuń z drzewa węzeł z kluczem key