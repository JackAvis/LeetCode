class Solution(object):
    def partition(self, s):
        palindromePartitions = []
        def isPalindrome(string):
            l = 0
            r = len(string) - 1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        def recurse(partition, start):
            if partition:
                if not isPalindrome(partition[-1]):
                    return
            if len("".join(partition)) == len(s):
                palindromePartitions.append(list(partition))
                return
            for character in range(start, len(s)):
                partition.append(s[start:character + 1])
                recurse(partition, character + 1)
                partition.pop()

        recurse([], 0)
        return palindromePartitions