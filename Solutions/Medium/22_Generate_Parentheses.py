class Solution(object):
    def generateParenthesis(self, n):
        combinations = []
        def backtrack(combination, openParen, pairs):
            if pairs == n:
                combinations.append("".join(combination))
                return
            if openParen == 0 :
                combination.append("(")
                backtrack(combination, openParen + 1, pairs)
                combination.pop()
            elif openParen == n - pairs:
                combination.append(")")
                backtrack(combination, openParen - 1, pairs + 1)
                combination.pop()
            else:
                combination.append("(")
                backtrack(combination, openParen + 1, pairs)
                combination.pop()
                combination.append(")")
                backtrack(combination, openParen - 1, pairs + 1)
                combination.pop()
        backtrack([], 0, 0)
        return combinations