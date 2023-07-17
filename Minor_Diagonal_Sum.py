class Solution:
    @staticmethod
    def Minor_Diagonal_Sum(array,row):
        col=len(array[0])
        i,j,Sum=0,col-1,0
        while i<row and j>=0:
            Sum+=array[i][j]
            i+=1
            j-=1
        return Sum
"""
You are given a N X N integer matrix. You have to find the sum of all the minor diagonal elements of A.
Minor diagonal of a M X M matrix A is a collection of elements A[i, j] such that i + j = M + 1 (where i, j are 1-based).
"""

if __name__ == '__main__':
    row=int(input())
    array=[]
    for _ in range(row):
        col=list(map(int,input().split()))
        array.append(col)
    print(Solution().Minor_Diagonal_Sum(array,row))