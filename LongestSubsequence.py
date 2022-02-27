class LongestSubsequence():
    def __init__(self,x,y):
        self.x = x 
        self.y = y 

    def lcs(self,n,m):
        if(n==0 or m==0):
            return 0

        if((n>0 and m>0) and (self.x[n-1] == self.y[m-1])):
            return 1+self.lcs(n-1,m-1)

        else:
            return max(self.lcs(n-1,m),self.lcs(n,m-1))

x = input("Enter first sequence: ")
y = input("Enter second sequence: ")

lcs = LongestSubsequence(x,y)
print("Length of the longest subsequence is: ",lcs.lcs(len(x),len(y)))