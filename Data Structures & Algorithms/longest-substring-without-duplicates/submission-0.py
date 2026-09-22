class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        curent_streak = set()
        max_string = 0
        
        for right in range(len(s)):
            char = s[right]
            
            while char in curent_streak:
                curent_streak.remove(s[left])
                left +=1
            
            curent_streak.add(char)
            
            curent_diff = right - left + 1

            if curent_diff > max_string:
                max_string = curent_diff
        

        return max_string