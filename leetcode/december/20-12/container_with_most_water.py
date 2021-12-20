# 11. Container With Most Water
# Medium
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left =0
        right = len(height)-1
        width = right - left
        final = 0
        for w in range(width, 0, -1):   #Moving inwards --> want the width to keep on decreasing as we check the area
            if height[left]<height[right]:
                final = max(final,height[left]*w)
                left+=1                    # if left is smaller than right, no need to check left index with other index on the right, they will be lower as width decreases
            else:
                final = max(final,height[right]*w)
                right-=1
        return final
        
        
        
        
        
if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    left =0
    right = len(height)-1
    width = right - left
    final = 0
    for w in range(width, 0, -1):   #Moving inwards --> want the width to keep on decreasing as we check the area
        if height[left]<height[right]:
            final = max(final,height[left]*w)
            left+=1
        else:
            final = max(final,height[right]*w)
            right-=1
    print(final)
        