from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequence = defaultdict(int)

        for number in nums:
            frequence[number] +=1

        bucket = [[] for i in range(len(nums) + 1)]
        for key,value in frequence.items():        
            bucket[value].append(key)

        answer = []
        for i in range(len(bucket) -1, 0, -1):
            for n in bucket[i]:
                answer.append(n)
                if len(answer) == k:
                    return answer 