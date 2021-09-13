# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for ind, val in enumerate(s):
            if val not in (s[:ind] + s[ind+1:]):
                return ind
            
        return -1
            
        

if __name__ == "__main__":
    s = "leetcode"
    # print(s[:0] + s[1:])
    # Solution().firstUniqChar("leetcode")
    print(Solution().firstUniqChar("aabb"))