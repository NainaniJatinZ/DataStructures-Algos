class Solution(object):
    def sortedSquares(self, nums):
        n = [0]*len(nums)
        for i in range(len(nums)): # getting index till negative numbers
            if nums[i]>=0:
                break
        # now we have 2 sorted arrays, so we can use the code from merge sort
        # but one array is reverse 
        j = i-1
        k = i
        l = 0
        while j>=0 and k<len(nums):
            if nums[j]**2<nums[k]**2:
                n[l] = nums[j]**2
                j-=1
            else:
                n[l] =  nums[k]**2
                k+=1
            l+=1
        while j>=0:
            n[l] = nums[j]**2
            j-=1
            l+=1
        while k<len(nums):
            n[l] =  nums[k]**2
            k+=1
            l+=1
        return n