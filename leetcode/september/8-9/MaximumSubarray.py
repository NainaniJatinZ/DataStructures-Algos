class Solution(object):
    def maxSubArray(self, nums):
        total_pos = 0
        total_neg = -10000000
        maxi_sub = 0
        pos_exist =0 
        for i in range(len(nums)):
            if nums[i]>= 0:
                pos_exist = 1
            total_pos += nums[i]
            if total_neg < nums[i]:
                total_neg = nums[i]
            if maxi_sub < total_pos:
                maxi_sub = total_pos
            if total_pos < 0:
                total_pos = 0
        if pos_exist == 0:
            return total_neg
        return maxi_sub