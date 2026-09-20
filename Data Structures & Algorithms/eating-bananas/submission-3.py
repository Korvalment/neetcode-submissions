class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        opt_m = 0

        while start <= end:
            mid = (start + end) // 2

            time_counter = 0
            for pile in piles:
                time_counter += math.ceil(pile / mid)

            if time_counter > h:
                start = mid + 1
            
            elif time_counter <= h:
                opt_m = mid     
                end = mid-1

        return opt_m
       