class Solution(object):
    def lastStoneWeight(self, stones):
        first = 0 
        second = 0
        while len(stones) > 1:
            stones.sort()
            first = len(stones) - 1
            second = len(stones) - 2
            if stones[first] == stones[second]:
                stones.pop(first)
                stones.pop(second)
            elif stones[first] > stones[second]:
                stones[first] = stones[first] - stones[second]
                stones.pop(second)  
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
                
            