class Solution(object):
    def isPowerOfFour(self, n):
        i = 0
        while i < n:
            if 4 ** i == n:
                return True
            elif 4 ** i > n:
                return False
            i += 1
        