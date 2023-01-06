
def bfs(inputGraph:dict,startingNode:any):
    if(inputGraph==None):
        return []
    result = []
    queue = [startingNode]
    while(len(queue)>0):
        current = queue.pop(0)
        result.append(current)
        for c in inputGraph[current]:
            queue.append(c)
    return result

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

print("Graph BFS Traversal Order: ",bfs(graph,'a'))