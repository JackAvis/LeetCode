from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq = 0
        for n in nums_set:
            # need to check if start of sequence
            if (n - 1) not in nums_set:
                seq_length = 1
                while (n + seq_length) in nums_set:
                    seq_length += 1
                longest_seq = max(longest_seq, seq_length)
        return longest_seq