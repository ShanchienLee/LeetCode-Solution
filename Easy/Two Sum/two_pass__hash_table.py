class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            a = target - nums[i]
            if a in hashmap and hashmap[a] != i:
                return[i, hashmap[a]]
            
