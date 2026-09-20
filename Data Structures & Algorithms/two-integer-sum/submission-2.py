from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targer_numbers = defaultdict(int)

        for index, number in enumerate(nums):

            if number in targer_numbers:

                return [targer_numbers[number],index]

            targer_number = target - number
            targer_numbers[targer_number] = index

        
            