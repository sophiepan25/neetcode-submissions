class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestLength = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while n + length in numSet:
                    length += 1

                if length > longestLength:
                    print('here')
                    longestLength = length
                
                print(length)
        return longestLength
            
        