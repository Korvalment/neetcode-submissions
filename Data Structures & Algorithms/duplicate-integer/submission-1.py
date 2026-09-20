from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq_number = set()
        for i in nums:
            if i in uniq_number:
                return True
            uniq_number.add(i)

        return False
            