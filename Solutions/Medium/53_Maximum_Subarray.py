class Solution(object):
    sol = float('-inf')

    def maxSubArray(self, nums):
        m = {}
        self.mSubArray(nums, 0, -1, m)
        return self.sol

    def mSubArray(self, nums, i, j, m):
        if i >= len(nums):
            return 0
        if i == j:
            return 0
        if i in m:
            return m[i]
        m[i] = nums[i] + max(self.mSubArray(nums, i + 1, i, m),
                             self.mSubArray(nums, i, i, m))
        if m[i] > self.sol:
            self.sol = m[i]
        return m[i]
