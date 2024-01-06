class Solution(object):
    def maxProduct(self, nums):
        maxi = 0
        mini = 0
        sol = 0 
        if len(nums) == 1:
            return nums[0]
        for num in range(len(nums)):
            tmp = maxi
            maxi = max(maxi * nums[num], nums[num], nums[num] * mini)
            sol = max(sol, maxi)
            mini = min(tmp * nums[num], nums[num], nums[num] * mini)
        return sol
        
        