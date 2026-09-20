class Solution:
    def twoSum(self, numbers, target: int):
        target_dict = {}

        for index, number in enumerate(numbers):
            curent_target = target - number

            if curent_target in target_dict:
                return [target_dict[curent_target]+1, index+1]

            target_dict[number] = index
