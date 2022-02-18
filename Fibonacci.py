def fiboRecur(n):
    if n<=2:
        return 1
    else:
        return fiboRecur(n-1) + fiboRecur(n-2)

print(fiboRecur(10))