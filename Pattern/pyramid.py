input = input("Enter the number of rows: ")
rows = int(input)


for i in range(rows):
    spaces = '.' * (rows - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)


for i in range(rows - 2, -1, -1):
    spaces = '.' * (rows - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)


