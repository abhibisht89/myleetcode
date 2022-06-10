class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i=0
        j=0
        maxx=0
        mp=dict()
        
        while j<len(s):
            if s[j] in mp:
                mp[s[j]]+=1
            else:
                mp[s[j]]=1
            
            if len(mp)>j-i+1:
                j+=1
            elif len(mp)==j-i+1:
                maxx=max(maxx,j-i+1)
                
            elif len(mp)<j-i+1:
                
                while len(mp)<j-i+1:
                    mp[s[i]]-=1
                    if mp[s[i]]==0:
                        del mp[s[i]]
                    i+=1
            j+=1
        return maxx        
                