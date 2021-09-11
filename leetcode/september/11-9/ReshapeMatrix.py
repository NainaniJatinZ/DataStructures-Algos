class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        m = len(mat)
        n = len(mat[0])
        k = 0
        l = 0
        Matrix = [[0 for x in range(c)] for y in range(r)] 
        if m*n != r*c:
            return mat
        for i in range(m):
            for j in range(n):
                if l==c:
                    l=0
                    k+=1
                Matrix[k][l] = mat[i][j]
                l+=1
        return Matrix 


         
        



if __name__ == "__main__":
    mat = [[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]]
    r = 6
    c = 2
    # print(len(mat[1]))
    print(Solution().matrixReshape(mat, r, c))