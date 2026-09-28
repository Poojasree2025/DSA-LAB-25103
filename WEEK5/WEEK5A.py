class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#poojasree av.sc.u4cse25103
class SinglyLinkedList:

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

    # ii) Insert at beginning
    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
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

    # iv) Insert at index
    def insert_at_index(self, data, index):
        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_begin(data)
            return

        new = Node(data)
        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Index out of range")
                return
            temp = temp.next

        if temp is None:
            print("Index out of range")
            return

        new.next = temp.next
        temp.next = new

    # v) Delete by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            print("Deleted value =", value)
            return

        temp = self.head

        while temp.next and temp.next.data != value:
            temp = temp.next

        if temp.next is None:
            print("Value not found")
        else:
            temp.next = temp.next.next
            print("Deleted value =", value)

    # vi) Delete first node
    def delete_first(self):
        if self.head is None:
            print("No Data to delete")
        else:
            temp = self.head
            self.head = self.head.next
            print("Deleted value =", temp.data)

    # vii) Delete last node
    def delete_last(self):
        if self.head is None:
            print("No Data to delete")
            return

        if self.head.next is None:
            print("Deleted value =", self.head.data)
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        print("Deleted value =", temp.next.data)
        temp.next = None

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
s = SinglyLinkedList()

while True:

    print("\n----- SINGLY LINKED LIST -----")
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
        s.create()

    elif choice == 2:
        data = int(input("Enter value: "))
        s.insert_begin(data)

    elif choice == 3:
        data = int(input("Enter value: "))
        s.insert_end(data)

    elif choice == 4:
        data = int(input("Enter value: "))
        index = int(input("Enter index: "))
        s.insert_at_index(data, index)

    elif choice == 5:
        value = int(input("Enter value to delete: "))
        s.delete_by_value(value)

    elif choice == 6:
        s.delete_first()

    elif choice == 7:
        s.delete_last()

    elif choice == 8:
        s.count_nodes()

    elif choice == 9:
        s.display()

    elif choice == 10:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
