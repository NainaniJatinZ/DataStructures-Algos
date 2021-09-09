class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # we have to back iterate because its replacing the first array and deleting values
        i = m-1
        j = n-1
        l = m+n-1
        while i>=0  and j>=0:
            if nums1[i]>nums2[j]:
                nums1[l] = nums1[i]
                i-=1
            else:
                nums1[l] =  nums2[j]
                j-=1
            l-=1
        # i loop not needed as the final array is nums1 
        while j>=0:
            nums1[l] =  nums2[j]
            j-=1
            l-=1

if __name__ == "__main__":
    hum1 = [0]
    hum2 = [1]
    n1 = 0
    n2 = 1
    Solution().merge(hum1, n1, hum2, n2)
    print(hum1)

