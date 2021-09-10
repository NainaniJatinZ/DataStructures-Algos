
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class WrongSolution(object): # going for min and max separately can give wrong sol if best diff is not with the min 
    # like [3,2,5,6,0,3] profit is 4 but this code gives 3
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        k = 0 
        mini = 100000
        maxi = -1
        for i in range(len(prices)-1):
            if prices[i]<mini:
                mini = prices[i]
                k = i
        while k < len(prices):
            if prices[k] > maxi:
                maxi = prices[k]
            k+=1
        if (maxi - mini) >= 0:
            return maxi - mini
        return 0

class Solution(object):
    def maxProfit(self, prices):
        mini = prices[0]
        res = 0
        for i in range(1, len(prices)):
            res = max(res, prices[i] - mini)
            mini = min(mini, prices[i])
        return res

if __name__ == "__main__":
    print(Solution().maxProfit([3,2,5,3,6,0,3]))
    