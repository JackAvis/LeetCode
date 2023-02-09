class Solution(object):
    def breakPalindrome(self, palindrome):
        if len(palindrome) == 1:
            return ""
        palindrome = list(palindrome)
        left = 0
        right = len(palindrome) - 1
        changed = False
        while left < len(palindrome):
            if palindrome[left] != 'a' and right != left:
                palindrome[left] = 'a'
                changed = True
                break
            left += 1
            right -= 1
        if not changed:
            palindrome[-1] = 'b'
        return "".join(palindrome)