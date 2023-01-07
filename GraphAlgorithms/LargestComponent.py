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

def dfs(graph:dict,startingNode:any,visited):
    if(startingNode in visited):
        return 0
    visited.add(startingNode)
    size = 1
    for neighbor in graph[startingNode]:
        size += dfs(graph,neighbor,visited)
    return size

def largestComponent(graph:dict):
    largest = 0
    visited = set()
    for node in graph.keys():
        length = dfs(graph,node,visited)
        if(largest<length):
            largest = length        
    return largest

edges = [['a','b'],['d','c'],['e','c'],['e','c'],['a','i'],['a','f'],['f','i']]
graph = edgeToGraph(edges)
print("Length of largest connected component in a graph: {}".format(largestComponent(graph)))


        
