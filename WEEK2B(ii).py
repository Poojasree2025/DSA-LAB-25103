arr = list(map(int, input("Enter array: ").split()))

arr.sort()

print("Sorted array:", arr)

key = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1

found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at position", mid + 1)
        found = True
        break

    elif key < arr[mid]:
        high = mid - 1

    else:
        low = mid + 1

if found == False:
    print("Element not found")