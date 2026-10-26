n = int(input("Enter diamond size (1 to 20): "))

if n < 1 or n > 20:
    print("Invalid size. Enter a number from 1 to 20.")
else:
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        if i == 1:
            print(spaces + "*")
        else:
            inside = " " * (2 * i - 3)
            print(spaces + "*" + inside + "*")

    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i)
        if i == 1:
            print(spaces + "*")
        else:
            inside = " " * (2 * i - 3)
            print(spaces + "*" + inside + "*")
