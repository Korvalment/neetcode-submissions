class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer_list = [1] *len(nums)

        left_number = 1
        for i in range(len(nums)):
            answer_list[i] *= left_number
            left_number = left_number *  nums[i]

        right_number = 1
        for i in range(len(nums)-1, -1, -1):
            answer_list[i] *= right_number
            right_number =right_number * nums[i]

        return answer_list
