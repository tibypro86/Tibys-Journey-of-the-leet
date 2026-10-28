class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        global_sum = nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            if current_sum + num > num:
                current_sum +=  num
            else:
                current_sum = num
            if current_sum > global_sum:
                global_sum = current_sum

        return global_sum