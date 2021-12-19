# 5958. Number of Smooth Descent Periods of a Stock

# You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

# A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

# Return the number of smooth descent periods.\
    

# Accepted

class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        counter = 0
        final = 0
        for first, second in zip(prices, prices[1:]):
            if first - second == 1:
                counter += 1
                continue
            for k in range(1, counter+1):
                final +=counter - k + 1
            counter = 0
        for k in range(1, counter+1):
                final +=counter - k + 1 
        final +=len(prices)
        return final
            
class Solution_better(object):      # example of temp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 1, 2, 3, 4]
    def getDescentPeriods(self, prices):  # as it goes through the list, it builds up the number if its smooth decreasing
        """
        :type prices: List[int]
        :rtype: int
        """
        temp = [1]
        for first, second in zip(prices, prices[1:]):
            if first - second ==1:
                temp.append(temp[-1]+1)
                print(temp)
            else:
                temp.append(1)
                print(temp)
        return sum(temp)
                
        
        
        
if __name__ == "__main__":
    
    prices =[12,11,10,9,8,7,6,5,4,3,4,3,10,9,8,7]
    # print(Solution().getDescentPeriods(prices))
    
    # temp =0
    # for k in range(1, 3+1):
    #     temp += 3 - k + 1
    # print(temp)
    # l = [1, 7, 3, 5]
        
            
    