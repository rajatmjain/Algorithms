from QuickSort import QuickSort as qs
def kSmallest(inputList,size,k):
    if size<=5:
        return qs(inputList)[k]
        

    

#     allMedians = []
#     allMediansLength = size//5
#     start = 0
#     for i in range(0,allMedians):
#         allMedians.append(inputList[start:start+5])
#         start += 5
    
#     print(allMedians)

# kSmallest([1,2,4,5,7],[3,462,442,11,43])


        