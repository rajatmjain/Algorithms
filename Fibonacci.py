def fiboRecur(n):
    if n<=2:
        return 1
    else:
        return fiboRecur(n-1) + fiboRecur(n-2)

print(fiboRecur(10))

def fiboDyn(n):
    f = [0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

print(fiboDyn(5))

def fiboDynSeed(n,seed1,seed2):
    f = [seed1,seed2]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n-1]

print(fiboDynSeed(5,3,7))
