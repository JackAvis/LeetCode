class Solution:
    def myPow(self, x: float, n: int) -> float:
        # consider naive solution
        # x = 2, n = 8
        # 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 = 2^8
        # split it in 2 -> 2^4 * 2^4 = 2^8
        # split in 2 -> 2^2 * 2^2

        # base case?
        def pow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            # negative?
            if n < 0:
                return 1 / pow(x, -n)
            if n % 2 == 0:
                halfPow = pow(x, n // 2)
                ans = halfPow * halfPow
                return ans
            else:
                halfPow = pow(x, (n-1) // 2)
                ans = halfPow * halfPow * x
                return ans
        return pow(x, n)