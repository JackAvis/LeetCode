class Solution(object):
    def merge(self, intervals):
        output = []
        insert_interval = []      
        intervals.sort()
        for i in intervals:
            if insert_interval == []:
                insert_interval = [i[0], i[1]]
            # no overlap, append candidate interval to output and redefine current interval to candidate interval
            elif insert_interval[1] < i[0]:
                output.append(insert_interval)
                insert_interval = [i[0], i[1]]
            # overlap case
            # candidate = [1, 3]
            # current = [2,6]
            # new candidate = [1, 6]
            # new_candidate = min(starts), max(ends)
            else:
                insert_interval = [min(insert_interval[0], i[0]), max(insert_interval[1], i[1])]
        # once we reach the end of the intervals, we append with the insert_interval
        output.append(insert_interval)
        return output
                
            

            

