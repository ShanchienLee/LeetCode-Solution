class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        sRight = sum(nums)
        sLeft = 0
        
        for i in range(len(nums)):
            sRight -= nums[i]
            if sLeft == sRight:
                return i
            sLeft += nums[i]
            
        return -1
