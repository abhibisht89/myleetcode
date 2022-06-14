class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cntlcs=self.lcs(word1,word2,len(word1),len(word2))
        
        ins=len(word1)-cntlcs
        dell=len(word2)-cntlcs
        
        return ins+dell
    
    def lcs(self,x,y,n,m):
        dp=[[0 for i in range(m+1)] for j in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if x[i-1]==y[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        
        return dp[n][m]