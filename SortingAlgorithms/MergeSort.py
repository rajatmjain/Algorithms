def merge(leftList,rightList):
    result = []
    i, j = 0,0
    while i<len(leftList) and j<len(rightList):
        if rightList[j] < leftList[i]:
            result.append(rightList[j])
            j += 1
        elif leftList[i] < rightList[j]:
            result.append(leftList[i])
            i += 1
    if len(leftList)==i:
        result.extend(rightList[j:])
    else:
        result.extend(leftList[i:])
    return result

def mergeSort(inputList):
    if len(inputList)<=1:
        return inputList
    
    left,right = mergeSort(inputList[:len(inputList)//2]),mergeSort(inputList[len(inputList)//2:])
    return merge(left,right)

print(mergeSort([1,3,52,4,6,7,0,-1,99,42,77]))   
    
