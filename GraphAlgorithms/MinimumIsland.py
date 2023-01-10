def islandCount(grid):
    visited = set()
    mini = float('inf')
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            length = dfs(grid,row,column,visited)
            if length<mini and length>0:
                mini = length
    return mini

def dfs(grid,row,column,visited):
    rowInbound = 0 <= row and row < len(grid)
    columnInbound = 0 <= column and column < len(grid[0])
    if(not rowInbound or not columnInbound):
        return 0

    if(grid[row][column]=='W'):
        return 0

    position = str(row)+":"+str(column)
    if position in visited:
        return 0
    visited.add(position)

    length = 1
    length += dfs(grid,row-1,column,visited)
    length += dfs(grid,row+1,column,visited)
    length += dfs(grid,row,column-1,visited)
    length += dfs(grid,row,column+1,visited)

    return length

# Grid creation
grid = [
    ['W','L','W','W','W'],
    ['W','L','W','W','W'],
    ['W','W','W','L','W'],
    ['W','L','L','L','W'],
    ['L','W','W','L','L'],
    ['L','L','W','W','W']
]

print("Minimum islands size is ",islandCount(grid))