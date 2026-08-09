class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        prevTemps = list()
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            currTemp = temperatures[i]
            while prevTemps and prevTemps[-1][0] < currTemp:
                index = prevTemps.pop()[1]
                result[index] = i - index
                
            prevTemps.append((currTemp, i))


        return result
                
        