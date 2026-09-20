class Solution:
    def maxArea(self, heights: List[int]) -> int:
        end = len(heights) -1
        start = 0
        maximum = 0

        while start < end:
            if heights[start] > heights[end]:
                curent_maximum = heights[end] * (end - start)
                end -=1
            else:
                curent_maximum = heights[start] * (end - start)
                start +=1

            if curent_maximum > maximum:
                maximum = curent_maximum            

        return maximum
