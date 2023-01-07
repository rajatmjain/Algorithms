def edgeToGraph(edges):
    graph = dict()
    for edge in edges:
        if(edge[0] not in graph.keys()):
            graph[edge[0]] = []
        if(edge[1] not in graph.keys()):
            graph[edge[1]] = []

        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    return graph


def shortestPath(graph:input,startingNode,destinationNode):
    queue = [[startingNode,0]]
    visited = set([startingNode])
    while(len(queue)>0):
        currentNode,distance = queue.pop(0)
        if currentNode == destinationNode:
            return distance
        for neighbor in graph[currentNode]:
            if(neighbor not in visited):
                queue.append([neighbor,distance+1])  
    return -1


edges = [
    ['w','x'],
    ['x','y'],
    ['z','y'],
    ['z','v'],
    ['w','v']
]

graph = edgeToGraph(edges)
print("Shortest path from w to z is: ",shortestPath(graph,'w','z'))

