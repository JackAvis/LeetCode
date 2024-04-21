from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet = []
        for i in range(len(position)):
            car_fleet.append((position[i], speed[i]))
        car_fleet.sort(key=lambda a: a[0])
        # calculate when the car will reach position
        # (target - pos) / speed = time to reach end
        numFleet = 0
        fleet_in_front_t = 0
        for i in range(len(car_fleet) -1, -1, -1):
            car = car_fleet[i]
            pos = car[0]
            speed = car[1]
            reach_end_t = (target  - pos) / speed
            # if a car takes longer than the fleet in front of it, then its a fleet itself
            # otherwise its going to bump into the fleet in front, aka fleet in front doesnt update
            # and a new fleet is not created
            if reach_end_t > fleet_in_front_t:
                numFleet += 1
                fleet_in_front_t = reach_end_t
        return numFleet