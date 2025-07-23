def sumEven(n):
    if n == 1:
        return 1
    else:
        return n * sumEven(n-1)

print("sum is",sumEven(5))