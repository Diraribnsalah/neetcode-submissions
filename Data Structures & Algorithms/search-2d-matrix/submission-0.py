class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix :
            return False
        m =  len(matrix)
        n = len(matrix[0])   
        left = 0
        right = n*m - 1
        while left <= right :
            mid = left + (right - left)//2
            current_value = matrix[mid // n][mid % n]
            if current_value == target :
                return True 
            elif current_value > target :
                right = mid - 1
            elif current_value < target :
                left = mid + 1

        return False
