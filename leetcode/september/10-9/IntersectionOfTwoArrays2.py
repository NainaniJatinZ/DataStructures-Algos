class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num = list()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                num.append(nums1[i])
                nums2.remove(nums1[i])

        return num




if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2]
    print(Solution().intersect(nums1, nums2))
    print(nums2)