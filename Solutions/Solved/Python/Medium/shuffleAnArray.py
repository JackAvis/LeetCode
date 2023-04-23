import random
# fisher-yates shuffle
class Solution:
    original: List[int]
    def __init__(self, nums: List[int]):
        self.original = nums

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        array = list(self.original)
        for i in range(len(array)):
            swapIndex = random.randint(0, i)
            # swap
            tmp = array[i]
            array[i] = array[swapIndex]
            array[swapIndex] = tmp
        return array
