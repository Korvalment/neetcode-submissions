class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) * len(matrix[0]) -1

        while start <= end:
            mid = (start + end) // 2
            current_arr = mid // len(matrix[0])
            current_ell = mid % len(matrix[0])

            if matrix[current_arr][current_ell] == target:
                return True

            elif matrix[current_arr][current_ell] > target:
                end  = mid - 1

            elif matrix[current_arr][current_ell] < target:
                start = mid + 1


        return False