class Solution(object):
    def searchRange(self, nums, target):
        l = 0
        r = len(nums) - 1
        sol = []
        i = 0
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] > target:
                r = mid - 1
            if nums[mid] == target:
                start = mid
                while mid >= 0 and nums[mid] == target:
                    mid -= 1
                mid += 1
                start = mid
                while mid < len(nums) and nums[mid] == target:
                    mid += 1
                end = mid - 1
                return [start, end]
        return [-1, -1]