class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

#poojasree av.sc.u4cse25103
class DoublyLinkedList:

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
            else:
                temp = self.head

                while temp.next:
                    temp = temp.next

                temp.next = new
                new.prev = temp

    # ii) Insert at beginning
    def insert_begin(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    # iii) Insert at end
    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new
            new.prev = temp

    # iv) Insert at index
    def insert_at_index(self, data, index):
        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_begin(data)
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Index out of range")
                return
            temp = temp.next

        if temp is None:
            print("Index out of range")
            return

        new = Node(data)

        new.next = temp.next
        new.prev = temp

        if temp.next is not None:
            temp.next.prev = new

        temp.next = new

    # v) Delete by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp is not None and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp.prev is not None:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev

        print("Deleted value =", value)

    # vi) Delete first node
    def delete_first(self):
        if self.head is None:
            print("No Data to delete")
        else:
            temp = self.head
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None

            print("Deleted value =", temp.data)

    # vii) Delete last node
    def delete_last(self):
        if self.head is None:
            print("No Data to delete")
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        if temp.prev is None:
            self.head = None
        else:
            temp.prev.next = None

        print("Deleted value =", temp.data)

    # viii) Count number of nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        print("Number of nodes =", count)

    # ix) Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head

            while temp:
                print(temp.data, end=" ")
                temp = temp.next

            print()


# Main Program
d = DoublyLinkedList()

while True:

    print("\n----- DOUBLY LINKED LIST -----")
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
        d.create()

    elif choice == 2:
        data = int(input("Enter value: "))
        d.insert_begin(data)

    elif choice == 3:
        data = int(input("Enter value: "))
        d.insert_end(data)

    elif choice == 4:
        data = int(input("Enter value: "))
        index = int(input("Enter index: "))
        d.insert_at_index(data, index)

    elif choice == 5:
        value = int(input("Enter value to delete: "))
        d.delete_by_value(value)

    elif choice == 6:
        d.delete_first()

    elif choice == 7:
        d.delete_last()

    elif choice == 8:
        d.count_nodes()

    elif choice == 9:
        d.display()

    elif choice == 10:
        print("Exiting...")
        break

    else:
        print("Invalid choice")