class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # looked at solution
        stack = []
        answers = [0 for i in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                topOfStack = stack.pop()
                indexCalc = i - topOfStack[1]
                answers[topOfStack[1]] = indexCalc
            stack.append((temp, i))
        return answers






