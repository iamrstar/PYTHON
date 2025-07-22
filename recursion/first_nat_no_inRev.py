def printN(n):
    if n > 0:
        printN(n-1)
        print(n, end=' ' ) 

def printNreverse(n):
    if n > 0:
        print(n, end=' ' ) 
        printNreverse(n-1)
printNreverse(10)