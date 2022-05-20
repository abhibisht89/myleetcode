class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        k=len(nums)-3
#         nums.sort()
        
        if len(nums)<3:return max(nums)
        
        # return nums[-3]
        
#         f=float("-inf")
#         s=float("-inf")
#         t=float("-inf")
        
#         for n in nums:
#             if n>f:
#                 t=s
#                 s=f
#                 f=n
#             elif n>s:
#                 t=s
#                 s=n
#             elif n>t:
#                 t=n
#         return t 

        def quickselect(nums,low,high,k):
            
            pivot=nums[high]
            ptr=low
            
            for i in range(low,high):
                if nums[i]<=pivot:
                    nums[i],nums[ptr]=nums[ptr],nums[i]
                    ptr+=1
            nums[ptr],nums[high]=nums[high],nums[ptr]
            
            if k==ptr:
                return nums[ptr]
            elif k<ptr:
                return quickselect(nums,low,ptr-1,k)
            else:
                return quickselect(nums,ptr+1,high,k)
        return quickselect(nums,0,len(nums)-1,k)     
                
                
                
        
        
