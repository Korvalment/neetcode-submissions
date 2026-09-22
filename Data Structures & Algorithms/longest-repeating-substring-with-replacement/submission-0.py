class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        counts = defaultdict(int)

        for right in range(len(s)):
            char = s[right]    
            counts[char] +=1

            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -=1
                left +=1

            if right - left + 1 > max_length:
                max_length = right - left + 1

        return max_length
