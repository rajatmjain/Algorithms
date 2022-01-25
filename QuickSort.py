def quickSort(inputList):
    if len(inputList)<=1:
        return inputList
    else:
        pivot = inputList.pop()
        lessThanPivot = []
        greaterThanPivot = []
        for element in inputList:
            if element<pivot:
                lessThanPivot.append(element)
            elif element>=pivot:
                greaterThanPivot.append(element)
        return quickSort(lessThanPivot) + [pivot] + quickSort(greaterThanPivot)

print(quickSort([1,5,2,7,4,6,23,12,9,7,1]))
            
        