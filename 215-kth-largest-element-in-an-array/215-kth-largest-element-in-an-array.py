class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]
        
        k=len(nums)-k
        
        def quickselect(low,high):
            pivot=nums[high]
            ptr=low
            
            for i in range(low,high):
                if nums[i]<=pivot:
                    nums[ptr],nums[i]=nums[i],nums[ptr]
                    ptr+=1
            nums[high],nums[ptr]=nums[ptr],nums[high]
            
            if k==ptr:
                return nums[ptr]
            elif k<ptr:
                return quickselect(low,ptr-1)
            else:
                return quickselect(ptr+1,high)
            
        return quickselect(0,len(nums)-1)   
                    