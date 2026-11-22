class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0 
        right = n - 1
        max_surface = 0
        while left < right :
            L = right - left 
            l = min(heights[left] , heights[right])
            current_surface = L * l 
            if heights[left] < heights[right] :
                left += 1
            else :
                right -= 1 

            if current_surface > max_surface :
                max_surface = current_surface


        return max_surface              