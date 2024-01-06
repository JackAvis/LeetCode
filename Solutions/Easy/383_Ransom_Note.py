class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        availableWords = {}
        for letter in magazine:
            if letter not in availableWords:
                availableWords[letter] = 1
            else:
                availableWords[letter] += 1
        for letter in ransomNote:
            if letter not in availableWords:
                return False
            elif availableWords[letter] == 0:
                return False
            availableWords[letter] -= 1
        return True
            
        