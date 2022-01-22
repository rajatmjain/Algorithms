def zeroPadding(numString,zeros,left=True):
    for i in range(zeros):
        if left:
            numString = '0' + numString
        else:
            numString = numString + '0'
    return numString

def karatsuba(x,y):
    x = str(x)
    y = str(y)
    if len(x)==1 and len(y)==1:
        return int(x)*int(y)
    
    if len(x)<len(y):
        x = zeroPadding(x,len(y)-len(x))
    elif len(x)>len(y):
        y = zeroPadding(y,len(y)-len(x))
    
    n = len(x)
    halfLength = n//2

    if (n % 2) != 0:
        halfLength += 1    
    BZeroPadding = n - halfLength
    AZeroPadding = BZeroPadding * 2

    a = int(x[:halfLength])
    b = int(x[halfLength:])
    c = int(y[:halfLength])
    d = int(y[halfLength:])

    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    k = karatsuba(a+b,c+d)

    A = int(zeroPadding(str(ac),AZeroPadding,False))
    B = int(zeroPadding(str(k-ac-bd),BZeroPadding,False))

    return A+B+bd

print(karatsuba(input("First number: "),input("Second number: ")))



        
            