
tree = []


def insert(x):
    if not tree:
        tree.append(x)
        return

    i = 0
    while i < len(tree):
        if tree[i] is None:
            tree[i] = x
            return
        if x == tree[i]:
            return
        if x < tree[i]:
            i = 2 * i + 1
        else:
            i = 2 * i + 2

    tree.extend([None] * (i - len(tree) + 1))
    tree[i] = x


def search(x):
    i = 0
    while i < len(tree) and tree[i] is not None:
        if tree[i] == x:
            return i
        if x < tree[i]:
            i = 2 * i + 1
        else:
            i = 2 * i + 2
    return -1


def inorder(i=0):
    if i < len(tree) and tree[i] is not None:
        inorder(2 * i + 1)
        print(tree[i], end=" ")
        inorder(2 * i + 2)


def preorder(i=0):
    if i < len(tree) and tree[i] is not None:
        print(tree[i], end=" ")
        preorder(2 * i + 1)
        preorder(2 * i + 2)


def postorder(i=0):
    if i < len(tree) and tree[i] is not None:
        postorder(2 * i + 1)
        postorder(2 * i + 2)
        print(tree[i], end=" ")


def delete(x):
    i = search(x)
    if i == -1:
        print("Not Found")
        return

    # Collect all values except the deleted value.
    values = [
        v for v in tree if v is not None and v != x
    ]

    tree.clear()
    for v in values:
        insert(v)


while True:
    print("\n1.Insert  2.Search  3.Delete")
    print("4.Inorder  5.Preorder  6.Postorder  7.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        insert(int(input("Enter value: ")))
    elif ch == 2:
        x = int(input("Enter value to search: "))
        print("Found" if search(x) != -1 else "Not Found")
    elif ch == 3:
        delete(int(input("Enter value to delete: ")))
    elif ch == 4:
        inorder()
        print()
    elif ch == 5:
        preorder()
        print()
    elif ch == 6:
        postorder()
        print()
    elif ch == 7:
        break
    else:
        print("Invalid choice")
