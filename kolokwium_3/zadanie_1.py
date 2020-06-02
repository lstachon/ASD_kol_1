# sprawdzam height i biore najwiekszy dla danych pól gdzie klocek ma byc polozony.
# zwikeszam height o 1 i dodaję kolocek w odpowiendnie przedziały podstawowe.
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.span = (0, 0)
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
def add_brick(node, interval, height):
    if node is None:
        return

    if includes(interval, node.span) and node.value == None:
        node.height = height
        return

    if node.value != None:
        if node.value > interval[0]:
            add_brick(node.left, interval, height)
        if node.value < interval[1]:
            add_brick(node.right, interval, height)
    return


# root, interval, int_number
def check_height_for_brick(node, interval, check_tab):
    if node is None:
        return

    if includes(interval, node.span) and node.value == None:
        check_tab.append(node.height)
        return

    if node.value != None:
        if node.value > interval[0]:
            # left
            check_height_for_brick(node.left, interval, check_tab)

        if node.value < interval[1]:
            # right
            check_height_for_brick(node.right, interval, check_tab)
    return


# lisc traktowany jako node z wartoscia None
def span(r, a, b):
    r.span = (a, b)
    if r.left is not None and r.right is not None:
        span(r.left, a, r.value)
        span(r.right, r.value, b)
    if r.right is None and r.left is not None:
        # right is NONe
        n1 = Node(None)
        r.right = n1
        n1.span = (r.value, r.span[1])
        span(r.left, a, r.value)

    if r.right is not None and r.left is None:
        n2 = Node(None)
        r.left = n2
        n2.span = (r.span[0], r.value)
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
            t[index].append((root.value, root.span, root.height))
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


# tworze drzeow bst, dla przedzialow podstawowych

# crrat bst tree for
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
    max_h = 0

    for i in T:

        check_tab = []
        check_height_for_brick(root, i, check_tab)

        # max_height so far
        v = max(check_tab)
        # height for new block old max heigh + 1
        new_v = v + 1

        if new_v > max_h:
            max_h = new_v

        add_brick(root, (i[0], i[1] + 1), new_v)

    return max_h


T = [(1, 3), (2, 5), (0, 3), (8, 9), (4, 6)]

r = create_tree(T)
print(r)
