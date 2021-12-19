# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

#A string is palindromic if it reads the same forward and backward.

# Accepted


class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in range(len(words)):
            # if words[i] == words[i][::-1]:
            #     return words[i]
            if self.isPalindrome(words[i]):
                return words[i]
        return ""
    
    def isPalindrome(self, s):
        l = len(s)
        if l < 2:
            return True
        elif s[0] == s[l - 1]:
            return self.isPalindrome(s[1: l - 1])
        
            
        
        
        
if __name__ == "__main__":


    words = ["abc","car","ada","racecar","cool"]
    print(Solution().firstPalindrome(words))
    # final.head = Solution1().deleteDuplicates(l1.head)
    # final.printlist()