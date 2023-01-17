class Solution(object):
    def rob(self, nums):
        def rob(nums, i, money, memo):
            if i in memo:
                # if we've already calculated the max money to gain at i, just add that value to the money we've gained so far
                return memo[i] + money
            if i >= len(nums):
                return money
            # money gained by not robbing 
            m1 = rob(nums, i + 1, money, memo)
            # money gained by robbing
            m2 = rob(nums, i + 2, money + nums[i], memo)
            # store the max money gained between the two
            memo[i] = max(m1, m2)
            return memo[i]
        # rob(0) returns max money gained from 0 to i
        return rob(nums, 0, 0, {})
            
