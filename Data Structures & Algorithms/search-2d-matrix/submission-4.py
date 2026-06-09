class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row
        top, bottom = 0, len(matrix) - 1

        row = 0

        while top <= bottom:
            mid = (top + bottom) // 2

            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                row = mid
                break
        
        # find column
        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2

            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                return True

        return False