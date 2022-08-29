class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        maxHeight = min(maxLeft, maxRight)
        maxWater = 0
        while left <= right:
            maxRight = max(height[right], maxRight)
            maxLeft = max(height[left], maxLeft)
            maxHeight = min(maxLeft, maxRight)
            maxWater = max(maxHeight * (right - left), maxWater)
            if maxRight < maxLeft:
                right -= 1
            else:
                left +=1                
        return maxWater
            
            