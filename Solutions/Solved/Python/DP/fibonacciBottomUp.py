class Solution(object):
    def fib(self, n):
        n_one = 0
        n_two = 1
        i = 0
        while i < n - 1:
            dp = n_one + n_two
            tmp = n_two
            n_two = dp
            n_one = tmp
            i += 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        return dp
            
            