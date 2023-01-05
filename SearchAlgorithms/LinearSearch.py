import random
def LinearSearch(data,target):
    for d in data:
        if d==target:
            return True
    return False

data = [i for i in range(1,10)]
target = random.randint(1,100)
print(data)
print(target)
print("Result: " + str(LinearSearch(data,target)))