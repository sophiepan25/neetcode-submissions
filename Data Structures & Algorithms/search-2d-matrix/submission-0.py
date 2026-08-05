class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1
        while l <= r:
            mid = l + (r-l)//2
            mid_row, mid_col = mid//cols, mid % cols
            value = matrix[mid_row][mid_col]
            if target == value:
                return True
            elif target > value:
                l += 1
            elif target < value:
                r -= 1
        return False

  

        
        