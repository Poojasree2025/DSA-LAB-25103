def search(arr, key, index):
    if index == len(arr):
        return False

    if arr[index] == key:
        return True

    return search(arr, key, index + 1)


ids = [101, 102, 103, 104, 105]

key = int(input("Enter employee ID to search: "))

if search(ids, key, 0):
    print("Employee ID found")
else:
    print("Employee ID not found")
