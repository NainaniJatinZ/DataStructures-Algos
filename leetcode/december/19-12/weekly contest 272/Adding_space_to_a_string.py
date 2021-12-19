#You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

# For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
# Return the modified string after the spaces have been added.

# Time limit 

class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        # temp = ""
        # for i in range(len(s)):
        #     if i in spaces:
        #         temp+=" "
        #     temp+=s[i]
        # return temp
        
        # counter = 0
        # for i in range(len(spaces)):
        #     if i<len(s)+counter:
        #         s = s[:spaces[i]+counter]+" "+s[spaces[i]+counter:]
        #         counter +=1
        # return s
        temp = []
        s1 = set(spaces)
        for i,k in enumerate(s):
            if i in s1:
                temp.append(" ")
            temp.append(k)
        return "".join(temp) # return string concatenation of strings in iterable

        
if __name__ == "__main__":
    
    s= "LeetcodeHelpsMeLearn"
    spaces = [8,13,15,24]
    print(Solution().addSpaces(s, spaces))
    # print(set(spaces))
     

