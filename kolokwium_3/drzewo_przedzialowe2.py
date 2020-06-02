# lisc jest nodem bez value
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.span = (0, 0)
        self.intervals = []


class IntervalTree:
    def __init__(self, root):
        self.root = root
    #
    # def insert(self, interval):
    #     a = interval[0]
    #     b = interval[1]
    #
    # def isLeaf(self, r):
    #     if r.value == None and r.left == None and r.right == None:
    #         return True
    #
    #     return False


def insert_bst(root, element):
    if root is None:
        root.value = element.value

    else:
        if root.value < element.value:
            if root.right is None:
                root.right = element
            else:
                insert_bst(root.right, element)
        else:
            if root.left is None:
                root.left = element
            else:
                insert_bst(root.left, element)


def includes(indetval1, interval2):
    # checking if interval 2 is in interval 1
    if interval2[0] >= indetval1[0] and indetval1[1] >= interval2[1]:
        return True
    return False


# root, interval, int_number
def add_interval(node, interval, int_number):
    if node is None:
        return

    if includes(interval, node.span):
        node.intervals.appepnd(int_number)
        print(node.span)
        return (node.value, node.span)

    if node.left is None and node.right is None:
        a, b = node.span
        # udoskonalic
        if includes(interval, (a, node.value)):
            print((a, node.value))
            return
        if includes(interval, (node.value, b)):
            print((node.value, b))
            return

    if node.value > interval[0]:
        # left
        add_interval(node.left, interval, int_number)

    if node.value < interval[1]:
        # right
        add_interval(node.right, interval, int_number)


# def query(node, val):


#
# def find_span(node, a, b):
#     l, r = node.span
#     if l >= a and r <= b:
#         return node.value
#
#     if node == None:
#         return
#
#     if a <= node.value and node.value <= b:
#         if node.left != None:
#             find_span(node.left, a, b)
#         if node.right != None:
#             find_span(node.right, a, b)
#     elif node.value < b:
#         if node.left != None:
#             find_span(node.left, a, b)
#     elif node.value > a:
#         if node.right != None:
#             find_span(node.right, a, b)


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
            t[index].append((root.value, root.span))
        else:
            t[index].append(root.value)
        index = index + 1
        prepare_to_print(root.left, t, index)
        prepare_to_print(root.right, t, index)
    return t


r = Node(10)
insert_bst(r, Node(5))
insert_bst(r, Node(15))
insert_bst(r, Node(0))
insert_bst(r, Node(7))
insert_bst(r, Node(12))
insert_bst(r, Node(20))

infp = 100
infm = -100

span(r, infm, infp)
printT(r)

print(find_span2(r, (5, 12)))
