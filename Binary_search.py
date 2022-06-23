from typing import List
class Solution:
    def search(self, nums:List[int], target:int)-> int:
        x = -1
        for i in range(0,len(nums)):
            if nums[i] == target:
                x = i
                break
        return x

#validation
nums = [-1]
target = -1

c = Solution()
print(c.search(nums, target))

