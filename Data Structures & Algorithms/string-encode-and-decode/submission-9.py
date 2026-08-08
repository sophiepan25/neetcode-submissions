class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        result = []
        i = 0

        while i < len(s):
            start_num = i
            while s[i] != "#":
                print(i)
                i += 1
            end_num = i
            length = int(s[start_num:end_num])
            start_str = end_num + 1
            end_str = start_str + length
            result.append(s[start_str:end_str])
            i = end_str
        return result

