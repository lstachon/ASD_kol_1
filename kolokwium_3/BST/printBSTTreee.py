def printT(table):
    l = len(table)
    for i in table:
        if len(i) > 0:
            print(i)

def prepare_to_print(root, t, index):
    if root:
        if len(t) >= index:
            t.append([])
            t[index].append((root.key, root.value))
        else:
            t[index].append((root.key, root.value))
        index = index + 1
        prepare_to_print(root.left, t, index)
        prepare_to_print(root.right, t, index)
    return t

bstdict = BSTDict()

bstdict.insert(10,"siusiak")
bstdict.insert(11,"ciapek")
bstdict.insert(9,"czucza")

a = prepare_to_print(bstdict.tree, [], 0)
printT(a)