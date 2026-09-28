class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#poojasree av.sc.u4cse25103

class CircularLinkedList:

    def __init__(self):
        self.head = None

    # i) Create linked list
    def create(self):
        n = int(input("Enter number of elements: "))

        for i in range(n):
            data = int(input("Enter value: "))
            new = Node(data)

            if self.head is None:
                self.head = new
                new.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                temp.next = new
                new.next = self.head

    # ii) Insert at beginning
    def insert_begin(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            new.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            new.next = self.head
            temp.next = new
            self.head = new

    # iii) Insert at end
    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            new.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new
            new.next = self.head

    # iv) Insert at index
    def insert_at_index(self, data, index):
        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_begin(data)
            return

        if self.head is None:
            print("Index out of range")
            return

        temp = self.head

        for i in range(index - 1):
            temp = temp.next

            if temp == self.head:
                print("Index out of range")
                return

        new = Node(data)
        new.next = temp.next
        temp.next = new

    # v) Delete by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        # If only one node exists
        if self.head.data == value and self.head.next == self.head:
            self.head = None
            print("Deleted value =", value)
            return

        # If first node contains the value
        if self.head.data == value:
            self.delete_first()
            return

        temp = self.head

        while temp.next != self.head and temp.next.data != value:
            temp = temp.next

        if temp.next == self.head:
            print("Value not found")
        else:
            temp.next = temp.next.next
            print("Deleted value =", value)

    # vi) Delete first node
    def delete_first(self):
        if self.head is None:
            print("No Data to delete")
            return

        # Only one node
        if self.head.next == self.head:
            print("Deleted value =", self.head.data)
            self.head = None
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        print("Deleted value =", self.head.data)

        self.head = self.head.next
        temp.next = self.head

    # vii) Delete last node
    def delete_last(self):
        if self.head is None:
            print("No Data to delete")
            return

        # Only one node
        if self.head.next == self.head:
            print("Deleted value =", self.head.data)
            self.head = None
            return

        temp = self.head

        while temp.next.next != self.head:
            temp = temp.next

        print("Deleted value =", temp.next.data)

        temp.next = self.head

    # viii) Count number of nodes
    def count_nodes(self):
        if self.head is None:
            print("Number of nodes = 0")
            return

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Number of nodes =", count)

    # ix) Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" ")
            temp = temp.next

            if temp == self.head:
                break

        print()


# Main Program
c = CircularLinkedList()

while True:

    print("\n----- CIRCULAR LINKED LIST -----")
    print("1. Create linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at index")
    print("5. Delete by value")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Count number of nodes")
    print("9. Display / Traverse")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        c.create()

    elif choice == 2:
        data = int(input("Enter value: "))
        c.insert_begin(data)

    elif choice == 3:
        data = int(input("Enter value: "))
        c.insert_end(data)

    elif choice == 4:
        data = int(input("Enter value: "))
        index = int(input("Enter index: "))
        c.insert_at_index(data, index)

    elif choice == 5:
        value = int(input("Enter value to delete: "))
        c.delete_by_value(value)

    elif choice == 6:
        c.delete_first()

    elif choice == 7:
        c.delete_last()

    elif choice == 8:
        c.count_nodes()

    elif choice == 9:
        c.display()

    elif choice == 10:
        print("Exiting...")
        break

    else:
        print("Invalid choice")