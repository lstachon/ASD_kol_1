
BLACK = 0
RED = 1
class RBNode:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.color = BLACK
        self.key = key
        self.value = value

def get_num_of_black_nodes(node):
    if node == None:
        return 0
    height_left = get_num_of_black_nodes(node.left)
    height_right = get_num_of_black_nodes(node.right)
    if node.color == BLACK:
        add = 1
    else:
        add = 0
    if height_left == -1 or height_right == -1 or height_left != height_right:
        return -1
    else:
        return height_left + add

def check_adj_red_nodes(node, lastColor):
    if node == None:
        return True
    if node.color == RED and lastColor == RED:
        return False
    return check_adj_red_nodes(node.left, node.color) and check_adj_red_nodes(node.right, node.color)


def checkRB(root):
    if root.color == RED:
        return False
    if not check_adj_red_nodes(root, BLACK):
        return False
    if get_num_of_black_nodes(root) != -1:
        return True
    else:
        return False

#testy:
root = RBNode(20, 2)
root.left = RBNode(30, 3)
root.right = RBNode(10, 1)
print(checkRB(root))

root = RBNode(20, 2)
root.left = RBNode(30, 3)
root.right = RBNode(10, 1)
print(checkRB(root))



root = RBNode(7,2)
root.left = RBNode(3,5)
root.right = RBNode(18,10)
root.right.color = RED
root.right.right =RBNode(22,88)
root.right.left = RBNode(10,99)
root.right.right.right = RBNode(26,881)
root.right.right.right.color = RED
root.right.left.left = RBNode(8,8811)
root.right.left.left.color = RED
root.right.right.right = RBNode(26,881)
root.right.right.right.color = RED
#
# root = RBNode(20, 2)
# root.left = RBNode(30, 3, RED)
# root.left.left = RBNode(10, 1, RED)
# print(checkRB(root))
#
# root = RBNode(20, 2)
# root.left = RBNode(30, 3)
# root.left.left = RBNode(10, 1)
# print(checkRB(root))
#
# root = RBNode(20, 2)
# root.left = RBNode(30, 3, RED)
# root.left.left = RBNode(10, 1)
# print(checkRB(root))
#
# root = RBNode(20, 2, RED)
# root.left = RBNode(30, 3)
# root.left.left = RBNode(10, 1)
# print(checkRB(root))