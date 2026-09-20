class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        absolute_sequence = 1
        bigest_sequence = 1
        set_nums = set(nums)

        if not nums:
            return 0

        for num in set_nums:
            if num-1 in set_nums:
                continue

            curent_num = num
            while curent_num + 1 in set_nums:
                bigest_sequence += 1
                curent_num +=1
                if bigest_sequence > absolute_sequence:
                    absolute_sequence = bigest_sequence

            bigest_sequence = 1

        return absolute_sequence