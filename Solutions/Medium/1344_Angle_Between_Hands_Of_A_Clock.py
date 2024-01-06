import math
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        convertedHour = hour / 12 + (minutes / 60) / 12
        if convertedHour > 1:
            convertedHour -= 1
        convertedMinute = minutes / 60 * 360
        convertedHour *= 360
        return min(abs(convertedHour - convertedMinute), abs(abs(convertedHour - convertedMinute) - 360))