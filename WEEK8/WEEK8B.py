

class Node:

    def __init__(self, data):

        self.data = data

        self.left = None

        self.right = None
 
 
def insert(root, data):

    new_node = Node(data)
 
    if root is None:

        return new_node
 
    queue = [root]
 
    while queue:

        temp = queue.pop(0)
 
        if temp.left is None:

            temp.left = new_node

            return root

        else:

            queue.append(temp.left)
 
        if temp.right is None:

            temp.right = new_node

            return root

        else:

            queue.append(temp.right)
 
 
def preorder(root):

    if root:

        print(root.data, end=" ")

        preorder(root.left)

        preorder(root.right)
 
 
def inorder(root):

    if root:

        inorder(root.left)

        print(root.data, end=" ")

        inorder(root.right)
 
 
def postorder(root):

    if root:

        postorder(root.left)

        postorder(root.right)

        print(root.data, end=" ")
 
 
root = None
 
for x in [10, 20, 30, 40, 50]:

    root = insert(root, x)
 
print("Preorder:")

preorder(root)
 
print("\nInorder:")

inorder(root)
 
print("\nPostorder:")

postorder(root)

 
