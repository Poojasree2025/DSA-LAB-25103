def fibonacci(a, b, n):
    if n == 0:
        return

    print(a, end=" ")
    fibonacci(b, a + b, n - 1)


n = int(input("Enter number of terms: "))

fibonacci(0, 1, n)