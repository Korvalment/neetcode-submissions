class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = set()

        for i in range(len(nums) -2):
            mid = i + 1
            end = len(nums) -1
            target = 0 - nums[i]


            while mid < end:
                if nums[mid] + nums[end] > target:
                    end -=1
                elif nums[mid] + nums[end] < target:
                    mid +=1
                else:
             
                    answer.add((nums[i], nums[mid], nums[end]))
                    mid +=1
                    end -=1

        return [list(i) for i in answer]