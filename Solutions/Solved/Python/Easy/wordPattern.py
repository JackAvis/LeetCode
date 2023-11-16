class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_to_word = {}
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            word = words[i]
            char = pattern[i]
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
        return len(set(char_to_word.values())) == len(char_to_word)
        
        