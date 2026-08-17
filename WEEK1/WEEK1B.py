def power(p, n):
    if n == 0:
        return 1
    else:
        return p * power(p, n - 1)

p = int(input("Enter p: "))
n = int(input("Enter n: "))

result = power(p, n)

print("Answer =", result)
