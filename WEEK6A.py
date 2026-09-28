class Stack:

    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    # Push
    def push(self, data):
        if self.top == self.size - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = data

    # Pop
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            data = self.stack[self.top]
            self.top -= 1
            print("Deleted value =", data)

    # Peek
    def peek(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            print("Top element =", self.stack[self.top])

    # Display
    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            for i in range(self.top, -1, -1):
                print(self.stack[i], end=" ")
            print()


# Main Program
size = int(input("Enter size of stack: "))
s = Stack(size)

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