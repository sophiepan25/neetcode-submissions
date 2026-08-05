class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers) - 1
        sum = numbers[first] + numbers[last]

        while sum != target:
            if sum < target:
                first += 1
            
            else:
                last -= 1

            sum = numbers[first] + numbers[last]
        
        return [first + 1, last + 1]
        