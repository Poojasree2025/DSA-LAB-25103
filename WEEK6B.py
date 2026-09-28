class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

#poojasree av.sc.u4cse25103
class Stack:

    def __init__(self):
        self.top = None

    # Push
    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new

    # Pop
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            temp = self.top
            print("Deleted value =", temp.data)
            self.top = self.top.next

    # Peek
    def peek(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            print("Top element =", self.top.data)

    # Display
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top

            while temp:
                print(temp.data, end=" ")
                temp = temp.next

            print()


# Main Program
s = Stack()

while True:

    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        data = int(input("Enter value: "))
        s.push(data)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        break

    else:
        print("Invalid choice")