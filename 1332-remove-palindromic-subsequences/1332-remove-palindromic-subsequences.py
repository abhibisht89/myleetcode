class Solution:
    def removePalindromeSub(self, s: str) -> int:
        #If the s is not pallindrome, it will always be reduced to empty string in 2 steps else it can         be reduce to empty string in 1 step.
        rev_str=s[::-1]
        
        if rev_str==s:
            return 1
        else:
            return 2