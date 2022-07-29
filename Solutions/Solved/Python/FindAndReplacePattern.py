class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        distinct_pattern  = self.findDict(pattern)
        sol = []
        for word in words:
            if self.findDict(word) == distinct_pattern:
                sol.append(word)
        return sol
        
    def findDict(self, word):
        d =  {}
        l = 0
        l_dict = {}
        for letter in range(len(word)):
            if word[letter] not in l_dict:  
                d[letter] = l
                l_dict[word[letter]] = l
                l += 1
            else:
                d[letter] = l_dict[word[letter]]
        return d
            
            