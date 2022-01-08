def QuickSort(inputList):
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
        return QuickSort(lessThanPivot) + [pivot] + QuickSort(greaterThanPivot)

print(QuickSort([1,5,2,7,4,6,23,12,9,7,1]))
            
        