

def printNodd(n):
    if n > 0:
        printNodd(n-1)
        print(2*n-1, end=' ' )
printNodd(5)