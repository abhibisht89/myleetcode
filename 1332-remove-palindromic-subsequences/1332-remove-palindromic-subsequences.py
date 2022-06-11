class Solution:
    def removePalindromeSub(self, s: str) -> int:
        #If the s is not pallindrome, it will always be reduced to empty string in 2 steps else it can         be reduce to empty string in 1 step.
        
        
#         rev_str=s[::-1]
        
#         if rev_str==s:
#             return 1
#         else:
#             return 2
        
        #complexity
        #Time - O(n)
        #Space - O(n) - space for reverse string
        
        if len(s)==0:
            return 0
        for i in range(len(s)//2):
            if s[i]!=s[len(s)-i-1]:
                return 2
        return 1 
    
        #complexity
        #Time - O(n)
        #Space - O(1) - space for reverse string