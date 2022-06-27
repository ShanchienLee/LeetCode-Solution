class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            a = target - nums[i]
            if a in hashmap and hashmap[a] != i:
                return[i, hashmap[a]]
            
#   先建立一個hashmap
#   用迴圈將value, index存進hashmap
#   用迴圈找出殘差a
#   以a值為key，於hashmap中帶出hashmap[a]值(實為array index)
#   條件hashmap[a]不等於i
#   回傳[i, hasmap[a]]
