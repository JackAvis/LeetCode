class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        smallestRanges = []
        curRange = []
        prevNum = 0
        if len(nums) == 0:
            return []
        for i in nums:
            if i - prevNum != 1 and i != nums[0]:
                if curRange[0] != prevNum:
                    curRange.append(prevNum)
                smallestRanges.append(curRange)
                curRange = []
            if curRange == []:
                curRange.append(i)
            prevNum = i
        if nums[-1] - prevNum != 1:
                if curRange[0] != prevNum:
                    curRange.append(prevNum)
                smallestRanges.append(curRange)
        sol = []
        for i in smallestRanges:
            r = ""
            if len(i) == 1:
                r += str(i[0])
            else:
                r += str(i[0]) + "->" + str(i[1])
            sol.append(r)
        return sol