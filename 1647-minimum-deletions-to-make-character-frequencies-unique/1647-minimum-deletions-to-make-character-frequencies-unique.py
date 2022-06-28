class Solution:
    def minDeletions(self, s: str) -> int:
            S = collections.Counter(s)
            count= 0
            unique = set()
            for char, freq in S.items():
                while freq >0 and freq in unique:
                    freq-=1
                    count+=1
                unique.add(freq)
            return count