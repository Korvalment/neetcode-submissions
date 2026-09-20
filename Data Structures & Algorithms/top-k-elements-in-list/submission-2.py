class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freguent_counter = defaultdict(int)

        for number in nums:
            freguent_counter[number] += 1

        buckets = [[] for i in range(len(nums) + 1)]
        for number, count in freguent_counter.items():
            buckets[count].append(number)

        for bucket in reversed(buckets):
            for number in bucket:
                result.append(number)

                if len(result) == k:
                    return result