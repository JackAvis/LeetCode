# Backtracking
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        paths = []
        self.dfs(digits, 0, [], paths)
        return paths
    def dfs(self, digits, i, s, paths):
        if len(s) == len(digits):
            if s != []:
                paths.append("".join(s))
            return
        if digits[i] == "7":
            chrs = ["p", "q", "r", "s"]
        elif digits[i] == "8":
            chrs = ["t", "u", "v"]
        elif digits[i] == "9":
            chrs = ["w", "x", "y", "z"]
        else:
            a = 97
            t = int(digits[i]) - 2
            start = (a + (t * 3))
            chr1 = chr(start)
            chr2 = chr(start + 1)
            chr3 = chr(start + 2)
            chrs = [chr1, chr2, chr3]
        for c in chrs:
            s.append(c)
            self.dfs(digits, i + 1, s, paths)
            s.pop()
            
        
            
            
        
