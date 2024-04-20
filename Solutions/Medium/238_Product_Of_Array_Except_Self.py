from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) runtime, O(1) space
        output = [0] * len(nums)
        prefix_prod = 1
        for i in range(len(output)):
            output[i] = prefix_prod
            prefix_prod *= nums[i]
        postfix_prod = 1
        for i in range(len(output) -1, -1, -1):
            output[i] *= postfix_prod
            postfix_prod *= nums[i]
        return output

    def productExceptSelfSolution1(self, nums: List[int]) -> List[int]:
        # O(n) space, O(n) runtime
        # construct prefix product arr
        prefix = []
        prefix_product = 1
        for num in nums:
            prefix_product *= num
            prefix.append(prefix_product)
        # construct postfix product arr
        postfix = [0] * len(nums)
        postfix_product = 1
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            postfix_product *= num
            postfix[i] = postfix_product
        # use the prefix and postfix to calc prod of array except self
        res = []
        for i in range(len(nums)):
            prefix_prod = 1
            postfix_prod = 1
            if i - 1 >= 0:
                prefix_prod = prefix[i - 1]
            if i + 1 < len(nums):
                postfix_prod = postfix[i + 1]
            res.append(prefix_prod * postfix_prod)
        return res
