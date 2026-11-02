

#AV.SC.U4CSE25103 POOJASREE

SIZE = 10

# 1. Separate Chaining
def separate_chaining(keys):
    table = [[] for i in range(SIZE)]

    for key in keys:
        index = key % SIZE
        table[index].append(key)

    print("\nSeparate Chaining:")
    for i in range(SIZE):
        print(i, ":", table[i])


# 2. Linear Probing
def linear_probing(keys):
    table = [None] * SIZE

    for key in keys:
        index = key % SIZE

        while table[index] is not None:
            index = (index + 1) % SIZE

        table[index] = key

    print("\nLinear Probing:")
    for i in range(SIZE):
        print(i, ":", table[i])


# 3. Quadratic Probing
def quadratic_probing(keys):
    table = [None] * SIZE

    for key in keys:
        index = key % SIZE
        i = 0

        while i < SIZE:
            new_index = (index + i * i) % SIZE

            if table[new_index] is None:
                table[new_index] = key
                break

            i += 1

        if i == SIZE:
            print("Could not insert", key)

    print("\nQuadratic Probing:")
    for i in range(SIZE):
        print(i, ":", table[i])


# Main Program
keys = list(map(int, input("Enter the keys: ").split()))

separate_chaining(keys)
linear_probing(keys)
quadratic_probing(keys)
