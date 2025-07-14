# Series Pattern Program
# Series: 1 2 3 4 10 5 6 7 8 26 9 10 11 12 42 ...

n = int(input("Please enter the number of terms: "))
series = []
current = 1

while len(series) < n:
    group = [current + i for i in range(4)]
    group_sum = sum(group)
    for val in group:
        if len(series) < n:
            series.append(val)
        else:
            break
    if len(series) < n:
        series.append(group_sum)
    current += 4

total = sum(series[:n])
print(f"So the total of first {n} terms of the series is {total}...")
print("End of the program...")
