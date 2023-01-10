def islandCount(grid):
    visited = set()
    count = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if(dfs(grid,row,column,visited)):
                count += 1
    return count

def dfs(grid,row,column,visited):
    rowInbound = 0 <= row and row < len(grid)
    columnInbound = 0 <= column and column < len(grid[0])
    if(not rowInbound or not columnInbound):
        return False

    if(grid[row][column]=='W'):
        return False

    position = str(row)+":"+str(column)
    if position in visited:
        return False
    visited.add(position)

    dfs(grid,row-1,column,visited)
    dfs(grid,row+1,column,visited)
    dfs(grid,row,column-1,visited)
    dfs(grid,row,column+1,visited)

    return True

# Grid creation
grid = [
    ['W','L','W','W','W'],
    ['W','L','W','W','W'],
    ['W','W','W','L','W'],
    ['W','L','L','L','W'],
    ['L','W','W','L','L'],
    ['L','L','W','W','W']
]

print("Number of islands are ",islandCount(grid))