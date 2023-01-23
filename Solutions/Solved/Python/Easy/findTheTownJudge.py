class Solution(object):
    def findJudge(self, n, trust):
        # n == 1 edge case
        if n == 1:
            return n
        # create dict of people mapped to who they trust
        trustDict = {}
        # create dict of people mapped to who they are trusted by
        trustedDict = {}
        for i in range(len(trust)):
            truster = trust[i][0]
            trusted = trust[i][1]
            if truster not in trustDict:
                trustDict[truster] = set()
                trustDict[truster].add(trusted)
            else:
                trustDict[truster].add(trusted)
            if trusted not in trustedDict:
                trustedDict[trusted] = set()
                trustedDict[trusted].add(truster)
            else:
                trustedDict[trusted].add(truster)
        for i in range(1, n + 1):
            # if they are not in trust dict (they dont trust anyone) 
            # and have n - 1 people who trust them (the rest of the town) then they are the judge
            if i not in trustDict and i in trustedDict:
                if len(trustedDict[i]) == n-1:
                    return i
        return -1