class Solution(object):
    
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        
        for i in range(len(nums)):
            j = nums[i]
            k = 0
            while (j != 0):
                j = j // 10
                k+=1
            if k%2 ==0:
                count+=1
        return count