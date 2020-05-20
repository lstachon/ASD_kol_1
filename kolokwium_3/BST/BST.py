
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, element):
    if root is None:
        root.val = element.val

    else:
        if root.val < element.val:
            if root.right is None:
                root.right = element
            else:
                insert(root.right,element)
        else:
            if root.left is None:
                root.left = element
            else:
                insert(root.left, element)


def find(root, element):
    while root is not None:
        if root.val is element:
            return root.val
        elif root.val<element:
            root = root.right
        else:
            root = root.left
    return None


#com O(n)
def check_if_bst(node, down_size, upper_size):
    if node is None:
        return True

    if node.val<down_size or upper_size<node.val:
        return False

    return (check_if_bst(node.left,down_size,node.val-1) and check_if_bst(node.right,node.val+1,upper_size))

def print_tree(root, s):
    if root:
        print(s + str(root.val))
        print_tree(root.left,  ' ' + s)
        print_tree(root.right, s + ' ')


r = TreeNode(50)
insert(r, TreeNode(30))
insert(r, TreeNode(20))
insert(r, TreeNode(40))
insert(r, TreeNode(70))
insert(r, TreeNode(60))
insert(r, TreeNode(80))
insert(r, TreeNode(90))

def printT(table):
    l = len(table)
    for i in table:
        if len(i) > 0:
            print(i)

def prepare_to_print(root, t, index):
    if root:
        if len(t) >= index:
            t.append([])
            t[index].append(root.val)
        else:
            t[index].append(root.val)
        index = index + 1
        prepare_to_print(root.left, t, index)
        prepare_to_print(root.right, t, index)
    return t

a = [[0], [1,2], [1,2,3,4]]
b= prepare_to_print(r, [], 0)
printT(b)

print(check_if_bst(r,-100000,100000))

