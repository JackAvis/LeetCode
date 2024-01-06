class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search if num[middle] < nums[right] then min is between num[left] and num[middle] and vice versa
        # Check if num to left is less than num, then its the min
        
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < nums[middle - 1]:
                return nums[middle]
            if nums[middle] < nums[right]:
                right = middle - 1
            elif nums[middle] > nums[right]:
                left = middle + 1
                
        
        
        