def quicksort(a, low, high):
    if low < high:
        i = low
        j = high
        pivot = low
# Poojasree av.sc.u4cse25103
        while i < j:

            # Move i from left to right
            while i <= high and a[i] <= a[pivot]:
                i += 1

            # Move j from right to left
            while a[j] > a[pivot]:
                j -= 1

            # Swap elements if pointers have not crossed
            if i < j:
                a[i], a[j] = a[j], a[i]

        # Place pivot in its correct position
        a[j], a[pivot] = a[pivot], a[j]

        # Sort left part
        quicksort(a, low, j - 1)

        # Sort right part
        quicksort(a, j + 1, high)


# Main Program
a = list(map(int, input("Enter numbers to sort: ").split()))

n = len(a)

quicksort(a, 0, n - 1)

print("Sorted array:")
print(a)