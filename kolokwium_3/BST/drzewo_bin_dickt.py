#BST_dict

class BTSNode:
    def __init__(self , key , value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self , root = None):
        self.root = root
    def inseret(self ,key , value):
        new = BTSNode(key, value)
        root = self.root
        while root != None:
            if root.key == key:
                return "occupied"
            elif key < root.key:
                if root.left == None:
                    new.parent = root
                    root.left = new
                    return
                else:
                    root = root.left
            else:
                if root.right == None:
                    new.parent = root
                    root.right = new
                    return
                else:
                    root = root.right

    def find(self ,key):
        #root is an BSTNode
        root = self.root
        while root != None:
            if root.key == key:
                return root
            elif key < root.key:
                root = root.left
            else:
                root = root.right
        return None
    def remove(self , key):
        elem = self.find(key)
        if elem == None:
            return
        else:
            if elem.left == None and elem.right == None:
                if elem.parent.right == elem:
                    elem.parent.right = None
                if elem.parent.left == elem:
                    elem.parent.left = None
                del elem
                return
            elif elem.left != None and elem.right == None:
                if elem.parent.right == elem:
                    elem.parent.right = elem.left
                if elem.parent.left == elem:
                    elem.parent.left = elem.left
                del elem
            elif elem.left == None and elem.right != None:
                if elem.parent.right == elem:
                    elem.parent.right = elem.right
                if elem.parent.left == elem:
                    elem.parent.left = elem.right
                del elem
            else:
                succ = self.succ(elem)
                if succ.right != None:
                    right = succ.right
                    succ.key , right.key = right.key , succ.key
                    succ.value, right.value = right.value, succ.value
                succ.key , elem.key = elem.key , succ.key
                succ.value, elem.value = elem.value , succ.value
                del succ
    def min(self):
        root = self.root
        while root.left != None:
            root = root.left
        return root
    def max(self):
        root = self.root
        while root.right != None:
            root = root.right
        return root
    def succ(self , elem):
        if elem.right != None:
            elem = elem.right
            while elem.left != None:
                elem = elem.left
            return elem
        else:
            while elem.parent.right == elem:
                elem = elem.parent
            return elem.parent
    def pred(self , elem):
        if elem.left != None:
            elem = elem.left
            while elem.right != None:
                elem = elem.right
            return elem
        else:
            while elem.parent.left == elem:
                elem = elem.parent
            return elem.parent
root = BTSNode( 10 , 1)
table = BST(root)
table.inseret( 5 , 2)
table.inseret(  4, 3 )
table.inseret(  21, 4 )
table.inseret(  15, 5 )
table.inseret(  12, 6 )
table.inseret(  25, 7 )
table.inseret(  22, 8 )
table.inseret(  27, 9 )
table.inseret(  24, 10 )
elem  = table.find( 12)
print(elem.value)
table.remove(12)
elem = table.find(12)
print(elem)
elem  = table.find( 5 )
print(elem.value)
table.remove(5)
elem = table.find(5)
print(elem)
elem  = table.find( 25 )
print(elem.value)
table.remove(25)
elem = table.find(25)
print(elem)