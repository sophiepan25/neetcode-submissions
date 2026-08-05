import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = dict()
        for i in nums:
            frequencies[i] = frequencies.get(i, 0) + 1

        sort = sorted(frequencies.items(), key = lambda x: x[1], reverse = True)
        print(sort)

        result = []
        for i in range(k):
            result.append(sort[i][0])

        return result
