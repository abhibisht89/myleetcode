class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s=0
        e=0
        ms=0
        rs=0
        st=set()
        while e <=len(nums)-1:
            if nums[e] not in st:
                st.add(nums[e])
                rs+=nums[e]
                ms=max(rs,ms)
                e+=1
            else:
                st.remove(nums[s])
                rs-=nums[s]
                s+=1
        return ms        