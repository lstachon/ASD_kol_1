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
