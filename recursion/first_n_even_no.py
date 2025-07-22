

def printNodd(n):
    if n > 0:
        printNodd(n-1)
        print(2*n, end=' ' )
printNodd(5)