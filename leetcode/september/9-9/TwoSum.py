# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Brute Force method:
# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i == j:
#                 continue
#             if (nums[i] + nums[j] == target):
#                 return [i, j]
    
# print(twoSum([3,2,4], 6))

# Optimised method with dicts to look if remaining exists in list
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i,v in enumerate(nums):
            rem = target - v
            if rem in d.keys():
                return [d[rem],i]
            else:
                d[v] = i
