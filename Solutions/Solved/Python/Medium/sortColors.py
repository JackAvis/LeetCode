class Solution:
    def sortColors(self, nums: List[int]) -> None:
        numFreq = [0, 0, 0]
        for num in nums:
            numFreq[num] += 1
        i = 0 
        curColor = 0
        while i < len(nums):
            while numFreq[curColor] == 0:
                curColor += 1
            nums[i] = curColor
            numFreq[curColor] -= 1
            i += 1
        
