# Use min Heap to keep sorted in logN
import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        negative_piles = [ -x for x in piles]
        heapq.heapify(negative_piles)
        i = len(piles) - 1
        while k > 0:
            maxRocks = heapq.heappop(negative_piles)
            rocksRemoved = ceil(maxRocks / 2)
            heapq.heappush(negative_piles, maxRocks - rocksRemoved)
            k -= 1
        return -sum(negative_piles)