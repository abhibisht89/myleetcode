class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        if len(nums)==1:
            return nums[0]
        
#         arr=[0]*len(nums)
#         arr[0]=nums[0]
        
#         for i in range(1,len(nums)):
#             arr[i]=arr[i-1]+nums[i]
            
#         return arr  
        
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
            
        return nums    