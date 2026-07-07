class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        low=0
        high=(n*m)-1
        while high>=low:
            mid=low+((high-low)//2)
            i=mid//n
            j=mid%n
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                high=mid-1
            else:
                low=mid+1
        return False           
        