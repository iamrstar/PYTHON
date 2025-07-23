def sumN(n):
    if n == 1:
        return 1
    else:
        return n + sumN(n-1)

print("sum is",sumN(5))