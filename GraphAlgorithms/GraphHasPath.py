
def bfs(inputGraph:dict,startingNode:any,destinationNode:any):
    if(inputGraph==None or startingNode not in inputGraph.keys() or destinationNode not in inputGraph.keys()) :
        return False
  
    queue = [startingNode]
    while(len(queue)>0):
        current = queue.pop(0)
        if(current == destinationNode):
            return True
        for c in inputGraph[current]:
            queue.append(c)
    return False

def dfs(inputGraph:dict,startingNode:any,destinationNode:any):
    if(inputGraph==None or startingNode not in inputGraph.keys() or destinationNode not in inputGraph.keys()) :
        return False 
    stack = [startingNode]
    while(len(stack)>0):
        current = stack.pop()
        if current == destinationNode:
            return True
        for c in inputGraph[current]:
            stack.append(c) 
    return False

# Graph creation 
graph = dict()
graph['a'] = ['b','c']
graph['b'] = ['d']
graph['c'] = ['e']
graph['d'] = ['f']
graph['e'] = []
graph['f'] = ['a']

#Graph
#  a->c->e
#  | \
#  v  |
#  b  |
#  |  |
#  v  |
#  d->f 

testCases = [['a','f'],['b','a']]

for tc in testCases:
    print("There is a path from {} to {} using DFS: {} ".format(tc[0],tc[1],dfs(graph,tc[0],tc[1])))
    print("There is a path from {} to {} using BFS: {} ".format(tc[0],tc[1],bfs(graph,tc[0],tc[1])))
    print()