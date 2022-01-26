def partition(inputList,left,right):
    x = inputList[right]
    i = left

    for j in range(left,right):
        if inputList[j]<= x:
            inputList[i],inputList[j] = inputList[j],inputList[i]
            i += 1
    inputList[i],inputList[right] = inputList[right],inputList[i]

    return right

def kThSmallest(inputList,left,right,k):
    if (k>0 and k<=right-left+1):
        index = partition(inputList,left,right)

        if (index-left == k-1):
            return inputList[index]
        elif (index-left > k-1):
            return kThSmallest(inputList,left,index-1,k)
        else:
            return kThSmallest(inputList,index+1,right,k-index+left-1)

inp = [94, 82, 88, 12, 23, 61, 11, 13, 70, 37, 28, 31, 64, 6, 19, 32, 27, 38, 35, 21, 50, 91, 69, 57, 24, 93, 22, 43, 30, 67, 90, 48, 42, 65, 45]

print(kThSmallest(inp,0,len(inp)-1,6))
    