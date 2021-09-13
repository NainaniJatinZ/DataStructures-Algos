# Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# ACHIEVED 32ms, better than 93%



class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i, val in enumerate(ransomNote):
            if val in magazine:
                magazine = magazine.replace(val,"")
                print(magazine)
                continue
            return False
        return True
                
            




if __name__ == "__main__":
    s = "aa"
    y = "aab"
    # y = y.replace('a', "", 1)
    # print(y)
    # print(Counter(s))
    print(Solution().canConstruct(s, y))