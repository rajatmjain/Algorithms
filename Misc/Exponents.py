def power(x,y):
    if y == 0:
        return 1
    n = y//2
    temp = power(x,n)

    if y%2==0:
        return temp*temp
    else:
        return x*temp*temp

print(power(7111,73))
