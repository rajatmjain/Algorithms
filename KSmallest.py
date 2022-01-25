from QuickSort import quickSort as qs
def kSmallest(inputList,size,k):
    if size<=5:
        return qs(inputList)[k-1]
    
    groupOfFiveLists = []
    i = 0
    while i<size:
        end = i+5
        groupOfFiveLists.append(inputList[i:end])
        i = end
    
    allMedians = []
    for unsortedList in groupOfFiveLists:
        allMedians.append(qs(unsortedList)[2])
    
    allMedians = qs(allMedians)
    pivot = allMedians[len(allMedians)//2]
    m=0

    for index in range(0,size):
        if pivot==inputList[index]:
            m = index
    
    print(index)

    if k==index:
        return(index)
    elif k<index:
        return kSmallest(inputList[0:index],index,k)
    elif k>index:
        return kSmallest(inputList[index:],size-index,k-index)
    



print(kSmallest([94, 82, 88, 12, 23, 61, 11, 13, 70, 37, 28, 31, 64, 6, 19, 32, 27, 38, 35, 21, 50, 91, 69, 57, 24, 93, 22, 43, 30, 67, 90, 48, 42, 65, 45],35,2))


        