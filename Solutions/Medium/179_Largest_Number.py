from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def customSort(a, b):
            a_first = int(str(a) + str(b))
            b_first = int(str(b) + str(a))
            if a_first > b_first:
                return -1
            elif b_first > a_first:
                return 1
            else:
                return 0
        letter_cmp_key = cmp_to_key(customSort)
        nums.sort(key=letter_cmp_key)
        sol = ""
        for i in nums:
            sol += str(i)
        if sol[0] == "0":
            return "0"
        return sol

       