class Solution:

                
            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [[num] + subset for subset in result]
        return result
        
        