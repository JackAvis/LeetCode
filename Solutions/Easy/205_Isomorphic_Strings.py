class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        for i in range(len(s)):
            changeChar = t[i]
            if s[i] in s_map:
                if changeChar != s_map[s[i]]:
                    return False
            else:
                s_map[s[i]] = changeChar
        return len(set(s_map.values())) == len(s_map)
        