class Solution(object):
    def restoreIpAddresses(self, s):
        validIps = []
        # backtrack through all possible '.' placements to find valid ip's
        def formIps(ipString, ipNumberArray, numberCount):
            if ipNumberArray != []:
                if int(ipNumberArray[-1]) < 0 or int(ipNumberArray[-1]) > 255:
                    return
                if ipNumberArray[-1][0] == "0" and len(ipNumberArray[-1]) > 1:
                    return
            if ipString == "" and numberCount == 4:
                validIps.append(".".join(ipNumberArray))
                return
            if numberCount >= 4:
                return
            for i in range(len(ipString)):
                number = ipString[0:i + 1]
                ipNumberArray.append(number)
                formIps(ipString[i + 1:], ipNumberArray, numberCount + 1)
                ipNumberArray.pop()
        formIps(s, [], 0)
        return validIps