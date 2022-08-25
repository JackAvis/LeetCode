class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = 1
        runArray = [0] * len(nums)
        
        # On first pass, gather everything you need to multiply by the left 
        for i in range(len(nums)):
            runArray[i] = c
            c *= nums[i]
        
        sol = [0] * len(nums)
        cTwo = 1
        # On second pass, multiply everything you need on left with everything you need on right
        for i in range(len(nums) - 1, -1, -1):
            sol[i] = cTwo * runArray[i]
            cTwo *= nums[i]
        return sol
            
            
            
            