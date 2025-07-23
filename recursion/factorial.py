def sumFact(n):
    if n == 1:
        return 1
    else:
        return n * sumFact(n-1)

print("sum is",sumFact(5))