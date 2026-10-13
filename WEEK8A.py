class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size
 
    def insert(self, data, index=0):
        if index >= self.size:
            print("Tree is full")
            return
 
        if self.tree[index] is None:
            self.tree[index] = data
        else:
            print("Position occupied")
 
    def preorder(self, index=0):
        if index < self.size and self.tree[index] is not None:
            print(self.tree[index], end=" ")
            self.preorder(2 * index + 1)
            self.preorder(2 * index + 2)
 
    def inorder(self, index=0):
        if index < self.size and self.tree[index] is not None:
            self.inorder(2 * index + 1)
            print(self.tree[index], end=" ")
            self.inorder(2 * index + 2)
 
    def postorder(self, index=0):
        if index < self.size and self.tree[index] is not None:
            self.postorder(2 * index + 1)
            self.postorder(2 * index + 2)
            print(self.tree[index], end=" ")
 
    def display(self):
        print(self.tree)
 
 
bt = BinaryTree(7)
 
bt.insert(10, 0)
bt.insert(20, 1)
bt.insert(30, 2)
bt.insert(40, 3)
bt.insert(50, 4)
 
print("Array:")
bt.display()
 
print("Preorder:")
bt.preorder()
 
print("\nInorder:")
bt.inorder()
 
print("\nPostorder:")
bt.postorder()