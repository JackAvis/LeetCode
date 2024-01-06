class Solution(object):
    def distinctNames(self, ideas):
        ideaSet = set(ideas)
        suffixes = [set() for i in range(26)]
        for i in ideas:
            # increment index associated to the character which starts the suffix
            suffixes[ord(i[0]) - ord('a')].add(i[1:])
        # for a valid pair must fulfill 2 conditions 
        # not in the same bucket (doesnt start with the same char)
        # does not share the same suffix 
        names = 0
        sharedSuffixes = set()
        for i in range(25):
            for j in range(i + 1, 26):
                sharedSuffixes = (len(suffixes[j]) + len(suffixes[i])) - len(suffixes[i].union(suffixes[j]))
                names += 2 * (len(suffixes[j]) - sharedSuffixes) * (len(suffixes[i]) - sharedSuffixes)
        return names
        