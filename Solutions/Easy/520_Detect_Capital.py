class Solution(object):
    def detectCapitalUse(self, word):
        numCapitals = 0
        firstWordCapital = False
        for i in range(len(word)):
            if ord(word[i]) >= 65 and ord(word[i]) <= 90:
                numCapitals += 1
                if i == 0:
                    firstWordCapital = True
        if (numCapitals == len(word)) or (numCapitals == 0) or (firstWordCapital and numCapitals == 1):
            return True
        return False