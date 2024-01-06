class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        citations.sort()
        numCitations = len(citations)
        for i in range(len(citations)):
            if i != 0 and citations[i-1] != citations[i]:
                numCitations = len(citations) - i
            h = max(h, min(numCitations, citations[i]))
        return h



        