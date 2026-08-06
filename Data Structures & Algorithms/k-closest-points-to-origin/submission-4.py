import math
import heapq
class Solution:
    def eucDistance(self, x, y):
        return math.sqrt((x)**2 + (y)**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #insert to heap with distance as first element of tuple
        print(math.sqrt(4))
        heap = []
        for point in points:
            x = point[0]
            y = point[1]
            print(point)
            distance = self.eucDistance(x,y)
            heap.append((distance, [x,y]))
        heapq.heapify(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
        