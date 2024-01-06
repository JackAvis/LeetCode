class Solution(object):
    def isAlienSorted(self, words, order):
        order_map = {}
        for word in range(len(order)):
            if order[word] not in order_map:
                order_map[order[word]] = word
        for i in range(len(words) - 1):
            curWord = words[i]
            nextWord = words[i + 1]
            j = 0
            # if they are equal, move the j index until we reach a letter that is not equal, which will determine the correct order
            while j < min(len(curWord), len(nextWord)) and order_map[curWord[j]] == order_map[nextWord[j]]:
                j += 1
            # if the smaller word was completely iterated over, then curWord needs to be shorter than nextWord to be in order
            if j == min(len(curWord), len(nextWord)):
                if len(curWord) > len(nextWord):
                    return False
            if j < min(len(curWord), len(nextWord)):
                # otherwise, the first different word of curWord and nextWord need to be in order
                if order_map[curWord[j]] > order_map[nextWord[j]]:
                    return False
            j += 1
        return True