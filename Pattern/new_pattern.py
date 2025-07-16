n = 11  # total number of rows
m = (n + 1) // 2  # middle row

for i in range(1, n + 1):
    if i <= m:
        dots = i - 1
        chars = 2 * (m - i) + 1
    else:
        dots = n - i
        chars = 2 * (i - m) + 1

    letter = chr(64 + i)  # ASCII: 65 -> 'A', 66 -> 'B', ...
    print("." * dots + letter * chars)
