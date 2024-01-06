class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = {}
        ans = []
        ind = 0
        for i in strs:
            sortedString = ''.join(sorted(i))
            if sortedString not in sort:
                sort[sortedString] = ind
                ans.append([i])
                ind += 1
            else:
                ans[sort[sortedString]].append(i)        
        return ans
            
            