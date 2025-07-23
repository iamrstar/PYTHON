def sumNOdd(n):
    if n == 1:
        return 1
    else:
        return 2*n-1 + sumNOdd(n-1)

print("sum is",sumNOdd(5))