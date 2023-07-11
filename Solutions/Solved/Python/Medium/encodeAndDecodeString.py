class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # need to uniquely identify a list of strings 
        # encode it into a string
        encoded = ""
        for word in strs:
            encoded += str('|') + str(len(word)) + str('|') + word 
        return encoded
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        ans = []
        while i < len(s):
            # find word length
            char = s[i]
            wordLenString = ""
            i += 1
            while i < len(s) and s[i] != '|':
                wordLenString += s[i]
                i += 1
            i += 1
            counter = 0
            word = ""
            while i < len(s) and counter < int(wordLenString):
                word += s[i]
                i += 1
                counter += 1
            ans.append(word)
        return ans
