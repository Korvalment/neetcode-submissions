class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, nums in enumerate(nums):
            diference = target - nums
            if diference in prevMap:
                return [prevMap[diference],i]

            prevMap[nums] = i