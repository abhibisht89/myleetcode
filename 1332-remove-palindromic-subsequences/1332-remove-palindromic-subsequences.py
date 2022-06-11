class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        rev_str=s[::-1]
        if rev_str==s:
            return 1
        else:
            return 2