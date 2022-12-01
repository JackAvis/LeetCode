class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def numberOfVowels(s: str):
            vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
            numVowels = 0
            for char in s:
                if char in vowels:
                    numVowels += 1
            return numVowels
        firstHalf = s[0:len(s) // 2]
        secondHalf = s[len(s) // 2: len(s)]
        return numberOfVowels(firstHalf) == numberOfVowels(secondHalf)
        