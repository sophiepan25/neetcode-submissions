class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        currLongest = 0
        currLetters = set()
        left = 0
        for right in range(len(s)):
            while s[right] in currLetters:
                currLetters.remove(s[left])
                left += 1
                currLongest -= 1

            currLetters.add(s[right])
            currLongest += 1
            if currLongest > longest:
                longest = currLongest
        return longest


        