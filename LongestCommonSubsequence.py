#Dynamic Programming Approach
def LongestCommonSubsequence(X,Y):
    m = len(X)
    n = len(Y)

    #Let grid maintain the the lenght of the LCS of X and Y
    grid = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            #Boundary checking when either of the sequences are empty
            if(m==0 or n==0):
                grid[i][j] = 0
            #When characters in both the sequences at the position are same
            elif X[i-1] == Y[j-1]:
                grid[i][j] = 1+grid[i-1][j-1]
            else:
                grid[i][j] = max(grid[i-1][j],grid[i][j-1])
    
    #Printing the LCS

    #Right bottom corner
    ind = grid[m][n]
    subS = [""] * (ind+1)
    subS[ind] = ""

    k = m 
    l = n
    while k>0 and l>0:
        if X[k-1] == Y[l-1]:
            subS[ind-1] = X[k-1]
            k-=1
            l-=1
            ind-=1

        elif grid[k-1][l] > grid[k][l-1]:
            k-=1

        else:
            l-=1
    lcs = ""
    for s in subS:
        lcs += s
    return ("The longest common subsequence of %s and %s is %s, of length %d."%(X,Y,lcs,len(lcs)))

print(LongestCommonSubsequence("BCADBC","ACBDC"))




            

    