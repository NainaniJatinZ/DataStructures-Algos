# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        for i, val in enumerate(s):
            if val in t:
                t = t.replace(val,"",1)
                continue
            return False
        return True


if __name__ == "__main__":
    s = "anagram"
    t = "nlgaram"
    print(Solution().isAnagram(s, t))