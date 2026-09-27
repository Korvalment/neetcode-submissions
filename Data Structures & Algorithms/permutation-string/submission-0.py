class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        end = len(s1)
        

        while end <= len(s2):
            s1 = sorted(s1)
            window = sorted(s2[start:end])

            if s1 == window:
                return True
            
            start+=1
            end+=1
        
        return False
            
