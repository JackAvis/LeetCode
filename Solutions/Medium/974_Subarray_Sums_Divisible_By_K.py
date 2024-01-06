class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = [0 for _ in range(len(nums))]
        runningSum = 0
        for i in range(len(nums)):
            runningSum += nums[i] 
            prefixSum[i] = runningSum % k 
        # rarray - larray % k == 0
        # (rarray - larray ) % k == 0
        # rarray % k - larray % k == 0
        # rarray % k = larray % k
        m = {}
        sol = 0
        m[0] = 1
        for i in prefixSum:
            if i in m:
                sol += m[i]
                m[i] += 1
            else:
                m[i] = 1
        return sol

        