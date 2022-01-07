def insertionSort(inputList):

    for i in range(1,len(inputList)):
        elementToSort = inputList[i]

        while elementToSort < inputList[i-1] and i > 0:
            temp = inputList[i-1]
            inputList[i-1] = elementToSort
            inputList[i] = temp
            i -= 1
    return inputList

print(insertionSort([1,5,2,7,4,6,23,12,9,0,1]))