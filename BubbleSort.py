def BubbleSort(inputList):
    status = False
    while not status:
        status = True
        for i in range(0,len(inputList)-1):
            if inputList[i]>inputList[i+1]:
                status = False
                temp = inputList[i]
                inputList[i] = inputList[i+1]
                inputList[i+1] = temp

    return inputList

print(BubbleSort([1,5,2,7,4,6,23,12,9,7,1]))