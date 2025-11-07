from cs50 import get_int

range_1 = range(1, 9, 1)
while True:
    n = get_int("Height: ")
    if n in range_1:
        break

for x in range(0, n, 1):
    for y in range(0, n, 1):
        if x + y < n - 1:
            print(" ", end="")
        else:
            print("#", end="")
    print()
