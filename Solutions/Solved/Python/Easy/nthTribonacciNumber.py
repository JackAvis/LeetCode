class Solution(object):
    def tribonacci(self, n):
        # what do we need to calculate the nth tribonacci number?
        # use our subsolutions to build up to nth solution - dp tabulation
        # Tn = Tn-3 + Tn-2 + Tn-1
        # base case 
        T0 = 0
        T1 = 1
        T2 = 1
        if n == 0:
            return T0
        if n == 1 or n == 2:
            return T1
        TribNum = 0
        for i in range(3, n + 1):
            TribNum = T0 + T1 + T2
            # define t0, t1, t2 for next iteration
            tmp = T2
            T2 = TribNum
            tmp2 = T1
            T1 = tmp
            T0 = tmp2
        return TribNum
