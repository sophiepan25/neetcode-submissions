class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        myMap = dict()
        
        for word in strs:
            sortedStr = "".join(sorted(word))
            if sortedStr not in myMap:
                myMap[sortedStr] = [word]
            else:
                myMap[sortedStr].append(word)
        return list(myMap.values())

        
        