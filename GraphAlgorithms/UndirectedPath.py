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

def dfs(graph:dict,startingNode:any,destinationNode:any,visited):
    if(startingNode in visited):
        return False
    visited.add(startingNode)
    if(startingNode==destinationNode):
        return True

    for neighbor in graph[startingNode]:
        if(dfs(graph,neighbor,destinationNode,visited)):
            return True   
    return False




edges = [['i','j'],['k','i'],['m','k'],['k','l'],['o','n']]
graph = edgeToGraph(edges)
start = 'i'
destination = 'l'
print("Undirected path from {} to {} exists: {}".format(start,destination,dfs(graph,'i','l',set())))


        
