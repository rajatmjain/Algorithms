def leftCOM(weights):
    weights.sort(reverse=True)
    print(weights)
    weighted = 0
    total = 0
    for i in range(0,len(weights)):
        weighted += weights[i]*i
        total += weights[i]

    return weighted/total

print(leftCOM([10,2,3,4,12,2]))
