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
        return False
    visited.add(startingNode)

    for neighbor in graph[startingNode]:
        dfs(graph,neighbor,visited)
    return True

def connectedComponentsCount(graph:dict):
    count = 0
    visited = set()
    for node in graph.keys():
        if(dfs(graph,node,visited)):
            count += 1
    return count

edges = [['i','j'],['k','i'],['m','k'],['k','l'],['o','n']]
graph = edgeToGraph(edges)
print("Count of connected components in a graph: {}".format(connectedComponentsCount(graph)))


        
