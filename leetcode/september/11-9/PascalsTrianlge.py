class Solution(object):
    def factorial(self, n):        
        return 1 if (n==1 or n==0) else n * self.factorial(n - 1);

    def ncr(self, n, r):
        return (self.factorial(n)/(self.factorial(n-r)*self.factorial(r)))

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [[self.ncr(n, r) for r in range(n+1)] for n in range(numRows)]
        return pascal
    
    # ref: https://mathematics.laerd.com/maths/binomial-theorem-intro.php 



if __name__ == "__main__":
    nu = 4
    # print(Solution().ncr(2,1))
    print(Solution().generate(7))