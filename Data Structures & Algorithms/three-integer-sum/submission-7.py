class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        solutions = []
        print(sorted(nums))
        for i in range(len(nums)-2):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = sorted_nums[left] + sorted_nums[right]
                if sum == -(sorted_nums[i]):
                    solutions.append([sorted_nums[i], sorted_nums[left],                    
                                        sorted_nums[right]])
                    right -= 1#?? shift both
                    left += 1
                    while sorted_nums[left] == sorted_nums[left-1] and left < right:
                        left += 1
                elif sum < -(sorted_nums[i]):
                    left += 1
                elif sum > -(sorted_nums[i]):
                    right -= 1
                
        return solutions


        