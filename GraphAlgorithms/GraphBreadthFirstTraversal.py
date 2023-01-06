
def dfsIte(inputGraph:dict,startingNode:any):
    if(inputGraph==None):
        return []
    result = []
    stack = [startingNode]
    while(len(stack)>0):
        current = stack.pop()
        result.append(current)
        for c in inputGraph[current]:
            stack.append(c)
        
    return result

recResult = []
def dfsRec(inputGraph:dict,startingNode:any):
    if(inputGraph==None):
        return []
    recResult.append(startingNode)
    for neighbour in inputGraph[startingNode]:
        dfsRec(inputGraph,neighbour)
    return recResult

# Graph creation 
graph = dict()
graph['a'] = ['b','c']
graph['b'] = ['d']
graph['c'] = ['e']
graph['d'] = ['f']
graph['e'] = []
graph['f'] = []

#Graph
#  a->c->e
#  |
#  v  
#  b
#  |
#  v
#  d->f 

print("Graph Iterative DFS Traversal Order: ",dfsIte(graph,'a'))
print("Graph Recursive DFS Traversal Order: ",dfsRec(graph,'a'))


