class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1

        while start <= end:
            midl = (start + end) // 2

            if nums[midl] == target:
                return midl

            elif nums[midl] > target:
                end = midl -1
            else:
                start = midl + 1

        return -1
        