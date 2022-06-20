class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        W=words
        ans=set(W)
        for word in W:
            for i in range(1,len(word)): ans.discard(word[i:])
        return len("#".join(list(ans)))+1