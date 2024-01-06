class Solution(object):
    def lengthOfLIS(self, nums):
        end = len(nums) - 2
        dp = [1] * len(nums)
        if end < 0:
            return 1
        while end >= 0:
            dp[end] = self.process(end, dp, nums)
            end -= 1
        return max(dp) 
    def process(self, end, dp, nums):
        og = nums[end]
        end += 1
        max_diff = 0
        while end <= len(nums) - 1:
            if nums[end] > og:
                if dp[end] + 1 > max_diff:
                    max_diff = dp[end] + 1
            end += 1
        if max_diff != 0:
            return max_diff
        return 1
        