def sumSquare(n):
    if n == 1:
        return 1
    else:
        return n*n + sumSquare(n-1)

print("sum is",sumSquare(5))