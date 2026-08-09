class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleetsAhead = list()
        #store latest arrival time out of cars in fleet
        pos_speed = sorted(zip(position, speed), key = lambda x: x[0], reverse = True)

        for pos, s in pos_speed:
            arrivalTime = (target-pos)/s
            if not fleetsAhead or fleetsAhead[-1] < arrivalTime:
                fleetsAhead.append(arrivalTime)

        return len(fleetsAhead)
        