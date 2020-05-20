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

# gdy slownik nie jest pusty

def insert( self, key, value ):

# wstaw wartość value pod klucz key (jeśli klucz key
# już istnieje, to podmień przechowywaną wartość
# value
def remove( self, key ):





def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val)
        print_tree(root.right)

# usuń z drzewa węzeł z kluczem key