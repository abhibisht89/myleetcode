class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d=dict()
        for idx,i in enumerate(nums):
            rem=target-i
            if rem not in d:
                d[i]=idx
            else:
                return [idx,d[rem]]
        
         
        
        
          