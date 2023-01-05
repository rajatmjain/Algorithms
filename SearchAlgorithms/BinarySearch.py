import random
def binarySearchIterative(inputData,target):
    low = 0
    high = len(inputData)-1
    while low<=high:
        mid=(low+high)//2

        if target<inputData[mid]:
            high = mid-1
            

        elif target>inputData[mid]:
            low = mid + 1
            
        
        elif target == inputData[mid]:
            return True
        
    return False

def binarySearchRecursive(inputData,target,low,high):
    if low>high:
        return False
    else:
        mid = (low+high)//2
        if target < inputData[mid]:
            return binarySearchRecursive(inputData,target,low,mid-1)

        elif target > inputData[mid]:
            return binarySearchRecursive(inputData,target,mid+1,high)
        elif target == inputData[mid]:
            return True



    

data = [i for i in range(1,100,5)]
target = random.randint(1,100)
print(data)
print(target)
print("Iterative Results:" + str(binarySearchIterative(data,target)))
print("Recursive Results:" + str(binarySearchRecursive(data,target,0,len(data)-1)))


