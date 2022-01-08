def SelectionSort(inputList):
    
    for i in range(0,len(inputList)-1):
        minimum = i
        for j in range(i+1,len(inputList)):
            if inputList[j]<inputList[minimum]:
                minimum = j
        if minimum != i:
            inputList[minimum], inputList[i] = inputList[i], inputList[minimum]
                
    return inputList

print(SelectionSort([1,5,2,7,4,6,23,12,9,7,1]))