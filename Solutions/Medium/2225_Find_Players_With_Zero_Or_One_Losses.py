class Solution(object):
    def findWinners(self, matches):
        one = []
        zero = []
        match_dict = {}
        for i in matches:
            if i[0] not in match_dict:
                match_dict[i[0]] = 0
            if i[1] not in match_dict:
                match_dict[i[1]] = -1
            else:
                match_dict[i[1]] -= 1
        for player in match_dict:
            if match_dict[player] == 0:
                zero.append(player)
            if match_dict[player] == -1:
                one.append(player)
        zero.sort()
        one.sort()
        return [zero, one]
        