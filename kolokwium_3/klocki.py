class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.span = (0, 0)
        self.intervals = []
        self.height = 0


def insert_bst(root, element):
    if root.value == element.value:
        return

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
def add_interval(node, interval,tab):
    if node is None:
        return
    if includes(interval, node.span) and node.value == None:

        node.intervals.append(interval)
        #node.height = len(node.intervals)
        # print(node.span)
        #tab.append(node.height)
        return
    if node.value != None:
        if node.value > interval[0]:
            # left
            add_interval(node.left, interval,tab)

        if node.value < interval[1]:
            # right
            add_interval(node.right, interval,tab)
    return


def del_interval(node, interval, int_number):
    if node is None:
        return

    if includes(interval, node.span):
        node.intervals.remove(interval)

        return

    if node.value > interval[0]:
        # left
        del_interval(node.left, interval, int_number)

    if node.value < interval[1]:
        # right
        del_interval(node.right, interval, int_number)


def print_Intervals(node):
    if node != None:
        if len(node.intervals) > 0:
            print(node.intervals)
    return


# wypisuje numery intervałow ktore zawieraja numer 14
def query(node, val):
    if node is not None:
        if node.value is None:
            return

        while node is not None and node.value is not None:
            if node.value is not None:
                if node.value >= val:
                    node = node.left
                    print_Intervals(node)
                else:
                    node = node.right
                    print_Intervals(node)
    return


# lisc traktowany jako node z wartoscia None
def span(r, a, b):
    r.span = (a, b)
    if r.left is not None:
        span(r.left, a, r.value)
    if r.right is not None:
        span(r.right, r.value, b)
    if r.right is None and r.left is None:
        n1 = Node(None)
        n2 = Node(None)
        r.right = n2
        r.left = n1
        n1.span = (r.span[0], r.value)
        n2.span = (r.value, r.span[1])
        return


# PRINTING TREE

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
            t[index].append((root.value, root.span, root.intervals))
        else:
            t[index].append(root.value)
        index = index + 1
        prepare_to_print(root.left, t, index)
        prepare_to_print(root.right, t, index)
    return t


def sortedArrayToBST(arr, root, start, end):
    if start <= end:
        mid = start + ((end - start) // 2)
        element = Node(arr[mid])
        insert_bst(root, element)
        sortedArrayToBST(arr, root, start, mid - 1)
        sortedArrayToBST(arr, root, mid + 1, end)


def create_tree(T):
    Temp = []
    for i in range(0, len(T)):
        a, b = T[i]
        Temp.append(a)
        Temp.append(b)
    Temp.sort()
    arr = []
    if Temp[0] != Temp[1]:
        arr.append(Temp[0])
    for i in range(1, len(Temp)):
        x = Temp[i - 1]
        y = Temp[i]
        if x is not y:
            arr.append(y)

    mid = len(arr) // 2
    c = arr[mid]
    root = Node(c)
    sortedArrayToBST(arr, root, mid + 1, len(arr) - 1)
    sortedArrayToBST(arr, root, 0, mid - 1)
    infp = 99999
    infm = -99999

    span(root, infm, infp)
    tab = []
    for i in T:
        add_interval(root, i, tab)
    print(tab)

    return root


# def create_tree(l):
#     print(l)
#     max_e = l[0][0]
#     for i, j in l:
#         if max_e < j:
#             max_e = j
#     arr = [i for i in range(max_e)]
#     mid = len(arr) // 2
#     c = arr[mid]
#     root = Node(c)
#     sortedArrayToBST(arr, root, mid + 1, len(arr) - 1)
#     sortedArrayToBST(arr, root, 0, mid - 1)
#     infp = 99999
#     infm = -99999
#
#     printT(root)
#     print("==============")
#     span(root, infm, infp)
#     for i in l:
#         print(i)
#         add_interval(root, i)
#
#     return root


T = [(1, 3), (2, 5), (0, 3), (8, 9), (4, 6)]

# T = [(1,10),(3,7),(5,9),(10,12)]

# T = [(1, 2), (3, 4), (5, 6), (9, 10)]

r = create_tree(T)
printT(r)
#
# # r = Node(10)
# # insert_bst(r, Node(15))
# # insert_bst(r, Node(5))
# # insert_bst(r, Node(0))
# # insert_bst(r, Node(7))
# # insert_bst(r, Node(12))
# # insert_bst(r, Node(20))
# #
#
# add_interval(r, (5, 20), 1)
# print("=========")
# add_interval(r, (5, 12), 1)
# print("=========")
# add_interval(r, (12, 20), 1)
# print("=========")
#
# printT(r)
# print("=========")
# query(r, 2)
#
# del_interval(r, (1, 3), 1)
# print("=========")
#
# printT(r)
