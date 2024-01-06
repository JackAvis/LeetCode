# BFS
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = [(list(start), 0)]
        seen = set()
        bank = set(bank)
        gene = start
        while queue:
            g = queue.pop(0)
            gene = g[0]
            mutations = g[1]
            if ''.join(gene) == end:
                return mutations
            for letter in 'ACGT':
                for i in range(len(gene)):
                    tmp = gene[i]
                    gene[i] = letter
                    if ''.join(gene) in bank and ''.join(gene) not in seen:
                        queue.append((list(gene), mutations + 1))
                    seen.add(''.join(gene))
                    gene[i] = tmp
        return -1
                    
                
            
            
        