class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        h = len(nums)-1
        while l<=h:
            m = (h+l)//2 
            if nums[m]==target:
                if m-1>0 and nums[m-1]==target:
                    l=m+1
                else:
                    return m
            elif nums[m] > target:
                h=m-1
            else:
                l=m+1
        return -1    
        
        
if __name__ == "__main__":
    
    nums = [-1,0,3,5,9,12]
    target = 9
    print(Solution().search(nums, target))
    # print(6//2)